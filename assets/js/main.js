/**
 * PCCST501 Computer Networks — Course Portal Interactive Scripts
 * Faculty: Prof. Anju Markose | Dept. of CSE, VJCET
 */

document.addEventListener('DOMContentLoaded', () => {
    initThemeToggle();
    initCodeCopyButtons();
    initSubnetCalculator();
    initCrcTool();
    initLineCodingVisualizer();
    initCapacityCalculator();
    initLiveSearch();
});

// ==========================================
// 1. THEME TOGGLE (Dark / Light Mode)
// ==========================================
function initThemeToggle() {
    const savedTheme = localStorage.getItem('pccst501-theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    const toggleBtn = document.getElementById('theme-toggle-btn');
    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme');
            const next = current === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('pccst501-theme', next);
            updateThemeIcon(next);
            
            // Redraw active canvases with current theme palette
            if (typeof drawWaveforms === 'function') {
                drawWaveforms();
            }
        });
    }
}

function updateThemeIcon(theme) {
    const icon = document.getElementById('theme-toggle-icon');
    if (icon) {
        if (theme === 'dark') {
            icon.className = 'bi bi-sun-fill text-warning';
        } else {
            icon.className = 'bi bi-moon-stars-fill text-primary';
        }
    }
}

// ==========================================
// 2. CODE SNIPPET COPY TO CLIPBOARD
// ==========================================
function initCodeCopyButtons() {
    const copyBtns = document.querySelectorAll('.code-copy-btn');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const codeBody = btn.closest('.code-window').querySelector('.code-body');
            if (!codeBody) return;
            
            const textToCopy = codeBody.innerText;
            navigator.clipboard.writeText(textToCopy).then(() => {
                const originalText = btn.innerHTML;
                btn.innerHTML = '<i class="bi bi-check2"></i> Copied!';
                btn.classList.add('bg-success', 'text-white');
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.classList.remove('bg-success', 'text-white');
                }, 2000);
            });
        });
    });
}

// ==========================================
// 3. INTERACTIVE IPV4 SUBNET CALCULATOR
// ==========================================
function initSubnetCalculator() {
    const calcBtn = document.getElementById('btn-calc-subnet');
    if (!calcBtn) return;

    calcBtn.addEventListener('click', calculateSubnet);
    
    // Also calculate on pressing Enter
    const ipInput = document.getElementById('input-subnet-ip');
    if (ipInput) {
        ipInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') calculateSubnet();
        });
    }
}

function calculateSubnet() {
    const rawIp = document.getElementById('input-subnet-ip')?.value.trim();
    const prefix = parseInt(document.getElementById('input-subnet-prefix')?.value);
    const resultBox = document.getElementById('subnet-result-box');

    if (!rawIp || isNaN(prefix) || prefix < 0 || prefix > 32) {
        alert('Please enter a valid IPv4 address and CIDR prefix (0-32).');
        return;
    }

    const octets = rawIp.split('.').map(Number);
    if (octets.length !== 4 || octets.some(o => isNaN(o) || o < 0 || o > 255)) {
        alert('Invalid IPv4 address format (must be 4 octets 0-255).');
        return;
    }

    // Convert IP to 32-bit integer
    const ipInt = (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3];
    const maskInt = prefix === 0 ? 0 : (~0 << (32 - prefix)) >>> 0;
    const netInt = (ipInt & maskInt) >>> 0;
    const wildInt = (~maskInt) >>> 0;
    const bcastInt = (netInt | wildInt) >>> 0;

    const intToIp = (val) => [
        (val >>> 24) & 255,
        (val >>> 16) & 255,
        (val >>> 8) & 255,
        val & 255
    ].join('.');

    const netIp = intToIp(netInt);
    const maskIp = intToIp(maskInt);
    const wildIp = intToIp(wildInt);
    const bcastIp = intToIp(bcastInt);

    let firstHost = 'N/A';
    let lastHost = 'N/A';
    let usableHosts = 0;

    if (prefix === 31) {
        firstHost = intToIp(netInt);
        lastHost = intToIp(bcastInt);
        usableHosts = 2;
    } else if (prefix === 32) {
        firstHost = intToIp(netInt);
        lastHost = intToIp(netInt);
        usableHosts = 1;
    } else if (prefix < 31) {
        firstHost = intToIp(netInt + 1);
        lastHost = intToIp(bcastInt - 1);
        usableHosts = Math.pow(2, 32 - prefix) - 2;
    }

    if (resultBox) {
        resultBox.innerHTML = `
            <div class="row g-3">
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Network ID (CIDR)</span>
                        <strong class="text-primary fs-5">${netIp}/${prefix}</strong>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Subnet Mask</span>
                        <strong class="text-dark fs-5">${maskIp}</strong>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">First Usable Host</span>
                        <strong class="text-success fs-5">${firstHost}</strong>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Last Usable Host</span>
                        <strong class="text-success fs-5">${lastHost}</strong>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Directed Broadcast</span>
                        <strong class="text-danger fs-5">${bcastIp}</strong>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Total Usable Hosts</span>
                        <strong class="text-primary fs-5">${usableHosts.toLocaleString()}</strong>
                    </div>
                </div>
            </div>
        `;
        resultBox.classList.remove('d-none');
    }
}

// ==========================================
// 4. INTERACTIVE CRC GENERATOR & DETECTOR
// ==========================================
function initCrcTool() {
    const crcBtn = document.getElementById('btn-run-crc');
    if (!crcBtn) return;

    crcBtn.addEventListener('click', runCrcCalculation);
}

function runCrcCalculation() {
    const dataBits = document.getElementById('input-crc-data')?.value.trim();
    const polyBits = document.getElementById('input-crc-poly')?.value.trim();
    const resultBox = document.getElementById('crc-result-box');

    if (!dataBits || !polyBits || !/^[01]+$/.test(dataBits) || !/^[01]+$/.test(polyBits)) {
        alert('Please enter valid binary strings (0s and 1s only) for Data and Polynomial.');
        return;
    }

    if (polyBits.length < 2) {
        alert('Generator polynomial must have degree >= 1 (at least 2 bits).');
        return;
    }

    // XOR modulo-2 division
    function mod2div(dividend, divisor) {
        let pick = divisor.length;
        let tmp = dividend.slice(0, pick).split('');
        const divArr = divisor.split('');

        while (pick < dividend.length) {
            if (tmp[0] === '1') {
                for (let i = 1; i < divArr.length; i++) {
                    tmp[i - 1] = tmp[i] === divArr[i] ? '0' : '1';
                }
            } else {
                for (let i = 1; i < divArr.length; i++) {
                    tmp[i - 1] = tmp[i];
                }
            }
            tmp[divArr.length - 1] = dividend[pick];
            pick++;
        }

        if (tmp[0] === '1') {
            for (let i = 1; i < divArr.length; i++) {
                tmp[i - 1] = tmp[i] === divArr[i] ? '0' : '1';
            }
        } else {
            for (let i = 1; i < divArr.length; i++) {
                tmp[i - 1] = tmp[i];
            }
        }
        return tmp.slice(0, divArr.length - 1).join('');
    }

    const zerosToAppend = '0'.repeat(polyBits.length - 1);
    const appendedData = dataBits + zerosToAppend;
    const remainder = mod2div(appendedData, polyBits);
    const codeword = dataBits + remainder;

    if (resultBox) {
        resultBox.innerHTML = `
            <div class="alert alert-info border-0 shadow-sm">
                <h5 class="fw-bold mb-3"><i class="bi bi-shield-check"></i> CRC Computation Steps</h5>
                <ul class="list-unstyled mb-0">
                    <li class="mb-2"><strong>Data Word (D):</strong> <code class="fs-6">${dataBits}</code> (${dataBits.length} bits)</li>
                    <li class="mb-2"><strong>Generator Polynomial (G):</strong> <code class="fs-6">${polyBits}</code> (Degree $r = ${polyBits.length - 1}$)</li>
                    <li class="mb-2"><strong>Appended Data $(D \times 2^r)$:</strong> <code>${appendedData}</code></li>
                    <li class="mb-2"><strong>Calculated CRC Remainder (R):</strong> <span class="badge bg-warning text-dark fs-6">${remainder}</span></li>
                    <li class="mt-3"><strong>Transmitted Codeword (T = D + R):</strong> <span class="badge bg-success fs-6">${codeword}</span></li>
                </ul>
            </div>
        `;
        resultBox.classList.remove('d-none');
    }
}

// ==========================================
// 5. INTERACTIVE LINE CODING CANVAS VISUALIZER
// ==========================================
function initLineCodingVisualizer() {
    const drawBtn = document.getElementById('btn-draw-waveforms');
    if (!drawBtn) return;

    drawBtn.addEventListener('click', drawWaveforms);
    drawWaveforms(); // Initial draw on load
}

function drawWaveforms() {
    const canvas = document.getElementById('waveformCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const bitsInput = document.getElementById('input-line-bits')?.value.trim() || '01001110';
    
    if (!/^[01]+$/.test(bitsInput)) {
        alert('Please enter binary bits only (0s and 1s).');
        return;
    }

    const bitCount = bitsInput.length;
    const paddingLeft = 140;
    const paddingRight = 30;
    const bitWidth = Math.max(45, (canvas.width - paddingLeft - paddingRight) / bitCount);
    canvas.width = paddingLeft + paddingRight + bitWidth * bitCount;

    const schemes = ['NRZ-L', 'NRZ-I', 'Manchester', 'Diff. Manch.', 'AMI (Bipolar)'];
    const rowHeight = 70;
    canvas.height = schemes.length * rowHeight + 40;

    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const bgCol = isDark ? '#0f172a' : '#ffffff';
    const gridCol = isDark ? '#334155' : '#e2e8f0';
    const textCol = isDark ? '#f8fafc' : '#0f172a';
    const mutedCol = isDark ? '#94a3b8' : '#64748b';
    const waveCol = '#3b82f6';

    ctx.fillStyle = bgCol;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Draw Top Bit Labels
    ctx.fillStyle = textCol;
    ctx.font = 'bold 14px "Fira Code", monospace';
    ctx.textAlign = 'center';
    for (let i = 0; i < bitCount; i++) {
        const x = paddingLeft + i * bitWidth + bitWidth / 2;
        ctx.fillText(bitsInput[i], x, 25);

        // Vertical grid dotted line
        ctx.strokeStyle = gridCol;
        ctx.setLineDash([3, 3]);
        ctx.beginPath();
        ctx.moveTo(paddingLeft + i * bitWidth, 35);
        ctx.lineTo(paddingLeft + i * bitWidth, canvas.height - 10);
        ctx.stroke();
    }
    // Last line
    ctx.beginPath();
    ctx.moveTo(paddingLeft + bitCount * bitWidth, 35);
    ctx.lineTo(paddingLeft + bitCount * bitWidth, canvas.height - 10);
    ctx.stroke();
    ctx.setLineDash([]); // Reset dash

    schemes.forEach((scheme, idx) => {
        const yCenter = 50 + idx * rowHeight + rowHeight / 2;
        const vHigh = yCenter - 20;
        const vLow = yCenter + 20;
        const vZero = yCenter;

        // Label
        ctx.textAlign = 'right';
        ctx.font = 'bold 12px "Outfit", sans-serif';
        ctx.fillStyle = textCol;
        ctx.fillText(scheme, paddingLeft - 15, yCenter + 4);

        // Baseline (0V)
        ctx.strokeStyle = mutedCol;
        ctx.lineWidth = 0.8;
        ctx.beginPath();
        ctx.moveTo(paddingLeft, vZero);
        ctx.lineTo(paddingLeft + bitCount * bitWidth, vZero);
        ctx.stroke();

        // Draw Waveform Line
        ctx.strokeStyle = waveCol;
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        let prevY = null;

        if (scheme === 'NRZ-L') {
            for (let i = 0; i < bitCount; i++) {
                const xStart = paddingLeft + i * bitWidth;
                const xEnd = xStart + bitWidth;
                const y = bitsInput[i] === '0' ? vHigh : vLow;

                if (prevY !== null && prevY !== y) {
                    ctx.moveTo(xStart, prevY);
                    ctx.lineTo(xStart, y);
                } else if (i === 0) {
                    ctx.moveTo(xStart, y);
                }
                ctx.lineTo(xEnd, y);
                prevY = y;
            }
        } else if (scheme === 'NRZ-I') {
            let currLevel = vHigh;
            for (let i = 0; i < bitCount; i++) {
                const xStart = paddingLeft + i * bitWidth;
                const xEnd = xStart + bitWidth;
                if (bitsInput[i] === '1') {
                    currLevel = currLevel === vHigh ? vLow : vHigh;
                }
                if (prevY !== null && prevY !== currLevel) {
                    ctx.moveTo(xStart, prevY);
                    ctx.lineTo(xStart, currLevel);
                } else if (i === 0) {
                    ctx.moveTo(xStart, currLevel);
                }
                ctx.lineTo(xEnd, currLevel);
                prevY = currLevel;
            }
        } else if (scheme === 'Manchester') {
            for (let i = 0; i < bitCount; i++) {
                const xStart = paddingLeft + i * bitWidth;
                const xMid = xStart + bitWidth / 2;
                const xEnd = xStart + bitWidth;
                const firstY = bitsInput[i] === '0' ? vHigh : vLow;
                const secondY = bitsInput[i] === '0' ? vLow : vHigh;

                if (prevY !== null && prevY !== firstY) {
                    ctx.moveTo(xStart, prevY);
                    ctx.lineTo(xStart, firstY);
                } else if (i === 0) {
                    ctx.moveTo(xStart, firstY);
                }
                ctx.lineTo(xMid, firstY);
                ctx.lineTo(xMid, secondY);
                ctx.lineTo(xEnd, secondY);
                prevY = secondY;
            }
        } else if (scheme === 'Diff. Manch.') {
            let currY = vLow;
            for (let i = 0; i < bitCount; i++) {
                const xStart = paddingLeft + i * bitWidth;
                const xMid = xStart + bitWidth / 2;
                const xEnd = xStart + bitWidth;
                if (bitsInput[i] === '0') {
                    currY = currY === vHigh ? vLow : vHigh; // transition at start for 0
                }
                if (prevY !== null && prevY !== currY) {
                    ctx.moveTo(xStart, prevY);
                    ctx.lineTo(xStart, currY);
                } else if (i === 0) {
                    ctx.moveTo(xStart, currY);
                }
                ctx.lineTo(xMid, currY);
                currY = currY === vHigh ? vLow : vHigh;
                ctx.lineTo(xMid, currY);
                ctx.lineTo(xEnd, currY);
                prevY = currY;
            }
        } else if (scheme === 'AMI (Bipolar)') {
            let lastMark = vLow;
            for (let i = 0; i < bitCount; i++) {
                const xStart = paddingLeft + i * bitWidth;
                const xEnd = xStart + bitWidth;
                let y;
                if (bitsInput[i] === '0') {
                    y = vZero;
                } else {
                    lastMark = lastMark === vHigh ? vLow : vHigh;
                    y = lastMark;
                }
                if (prevY !== null && prevY !== y) {
                    ctx.moveTo(xStart, prevY);
                    ctx.lineTo(xStart, y);
                } else if (i === 0) {
                    ctx.moveTo(xStart, y);
                }
                ctx.lineTo(xEnd, y);
                prevY = y;
            }
        }
        ctx.stroke();
    });
}

// ==========================================
// 6. CHANNEL CAPACITY CALCULATOR
// ==========================================
function initCapacityCalculator() {
    const calcBtn = document.getElementById('btn-calc-capacity');
    if (!calcBtn) return;

    calcBtn.addEventListener('click', calculateChannelCapacity);
}

function calculateChannelCapacity() {
    const bw = parseFloat(document.getElementById('input-cap-bw')?.value);
    const snrDb = parseFloat(document.getElementById('input-cap-snr')?.value);
    const levels = parseInt(document.getElementById('input-cap-levels')?.value);
    const resultBox = document.getElementById('capacity-result-box');

    if (isNaN(bw) || isNaN(snrDb) || isNaN(levels) || bw <= 0 || levels < 2) {
        alert('Please enter valid numeric parameters (Bandwidth > 0, Levels >= 2).');
        return;
    }

    // Nyquist bit rate: 2 * B * log2(L)
    const nyquistRate = 2 * bw * Math.log2(levels);

    // Shannon capacity: B * log2(1 + 10^(snr_dB/10))
    const snrLinear = Math.pow(10, snrDb / 10.0);
    const shannonCapacity = bw * Math.log2(1 + snrLinear);

    const formatBps = (val) => {
        if (val >= 1e9) return (val / 1e9).toFixed(2) + ' Gbps';
        if (val >= 1e6) return (val / 1e6).toFixed(2) + ' Mbps';
        if (val >= 1e3) return (val / 1e3).toFixed(2) + ' kbps';
        return val.toFixed(2) + ' bps';
    };

    if (resultBox) {
        resultBox.innerHTML = `
            <div class="row g-3">
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Nyquist Max Bit Rate (Noiseless)</span>
                        <strong class="text-primary fs-5">${formatBps(nyquistRate)}</strong>
                        <div class="text-muted small mt-1">Formula: $2 \\times B \\times \\log_2(${levels})$</div>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-3 bg-light rounded-3 border">
                        <span class="text-muted small d-block">Shannon Channel Capacity (Noisy)</span>
                        <strong class="text-success fs-5">${formatBps(shannonCapacity)}</strong>
                        <div class="text-muted small mt-1">Linear SNR: ${snrLinear.toFixed(1)}</div>
                    </div>
                </div>
            </div>
        `;
        resultBox.classList.remove('d-none');
    }
}

// ==========================================
// 7. LIVE SEARCH FILTER
// ==========================================
function initLiveSearch() {
    const searchInput = document.getElementById('global-search-input');
    if (!searchInput) return;

    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const searchableItems = document.querySelectorAll('.searchable-item');

        searchableItems.forEach(item => {
            const text = item.innerText.toLowerCase();
            if (text.includes(query)) {
                item.style.display = '';
            } else {
                item.style.display = 'none';
            }
        });
    });
}
