/**
 * PCCST501 Computer Networks — Interactive Simulator Lab Suite
 * Faculty: Prof. Anju Markose | Dept. of CSE, VJCET
 */

document.addEventListener('DOMContentLoaded', () => {
    initSimTabs();
    initHttpSimulator();
    initDnsSimulator();
    initBitTorrentSimulator();
    initTcpHandshakeSimulator();
    initTcpCongestionSimulator();
    initSubnetSimulator();
    initDijkstraSimulator();
    initDistanceVectorSimulator();
    initSlidingWindowSimulator();
    initCrcSimulator();
    initHammingSimulator();
    initCsmaSimulator();
    initLineCodingSimulator();
    initCapacitySimulator();
    initSnmpSimulator();
    initLabVideoPlayers();
});

// ==========================================
// 0. TAB & CATEGORY NAVIGATION
// ==========================================
function initSimTabs() {
    const tabBtns = document.querySelectorAll('.sim-filter-btn');
    const simCards = document.querySelectorAll('.sim-card-wrapper');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.getAttribute('data-filter');
            simCards.forEach(card => {
                if (filter === 'all' || card.getAttribute('data-category') === filter) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
}

// ==========================================
// 1. MODULE 1: HTTP REQUEST/RESPONSE INSPECTOR
// ==========================================
function initHttpSimulator() {
    const sendBtn = document.getElementById('http-send-btn');
    if (!sendBtn) return;

    sendBtn.addEventListener('click', runHttpSimulation);
}

function runHttpSimulation() {
    const method = document.getElementById('http-method').value;
    const url = document.getElementById('http-url').value.trim();
    const version = document.getElementById('http-version').value;
    const connType = document.getElementById('http-connection').value;
    const bodyInput = document.getElementById('http-body').value.trim();

    const animTrack = document.getElementById('http-anim-track');
    const responseBox = document.getElementById('http-response-box');

    // Show Handshake and Transmission Animation
    animTrack.innerHTML = `
        <div class="alert alert-info py-2 px-3 small d-flex align-items-center gap-2 mb-2">
            <span class="spinner-border spinner-border-sm" role="status"></span>
            <span>Initiating TCP 3-Way Handshake with server on Port 80/443...</span>
        </div>
    `;

    setTimeout(() => {
        animTrack.innerHTML = `
            <div class="alert alert-primary py-2 px-3 small d-flex align-items-center justify-content-between mb-2">
                <span><i class="bi bi-arrow-right-circle-fill text-primary"></i> <strong>Client &rarr; Server:</strong> ${method} ${url} ${version}</span>
                <span class="badge bg-primary">Transmitting Payload</span>
            </div>
        `;
    }, 600);

    setTimeout(() => {
        // Generate Response based on request
        let status = '200 OK';
        let statusClass = 'success';
        let respContentType = 'text/html; charset=UTF-8';
        let respBody = '';

        if (url.includes('404') || url.includes('notfound')) {
            status = '404 Not Found';
            statusClass = 'danger';
            respBody = `<!DOCTYPE html><html><body><h1>404 Not Found</h1><p>The requested resource ${url} was not found on VJCET Web Server.</p></body></html>`;
        } else if (method === 'POST') {
            status = '201 Created';
            statusClass = 'success';
            respContentType = 'application/json';
            respBody = JSON.stringify({
                status: "success",
                message: "Payload received and processed by VJCET HTTP Server",
                receivedData: bodyInput || "{ default: 'no body' }",
                timestamp: new Date().toISOString()
            }, null, 2);
        } else if (url.endsWith('.pdf')) {
            status = '200 OK';
            respContentType = 'application/pdf';
            respBody = `[Binary Stream: 24,512 Bytes — PCCST501 Course Notes Content]`;
        } else {
            status = '200 OK';
            respBody = `<!DOCTYPE html>
<html lang="en">
<head><title>VJCET Course Server Response</title></head>
<body>
    <h1>Welcome to PCCST501 Computer Networks</h1>
    <p>Faculty: Prof. Anju Markose | Dept. of CSE</p>
    <p>Server Status: Active &bull; Protocol: ${version}</p>
</body>
</html>`;
        }

        const dateStr = new Date().toUTCString();
        const contentLen = respBody.length;

        const rawHeaders = `${version} ${status}
Date: ${dateStr}
Server: Apache/2.4.52 (Ubuntu Linux)
Connection: ${connType}
Content-Type: ${respContentType}
Content-Length: ${contentLen}
ETag: "5d8c72a-${contentLen.toString(16)}"
Strict-Transport-Security: max-age=31536000; includeSubDomains`;

        animTrack.innerHTML = `
            <div class="alert alert-success py-2 px-3 small d-flex align-items-center justify-content-between mb-2">
                <span><i class="bi bi-arrow-left-circle-fill text-success"></i> <strong>Server &rarr; Client:</strong> ${version} ${status}</span>
                <span class="badge bg-success">${status}</span>
            </div>
        `;

        responseBox.innerHTML = `
            <div class="card border-0 bg-dark text-light p-3 rounded-3 font-mono small">
                <div class="d-flex justify-content-between align-items-center border-bottom border-secondary pb-2 mb-2">
                    <span class="text-warning fw-bold"><i class="bi bi-terminal-fill"></i> HTTP Response Headers &amp; Body</span>
                    <span class="badge bg-${statusClass}">${status}</span>
                </div>
                <pre class="text-info mb-3" style="white-space: pre-wrap;">${rawHeaders}</pre>
                <div class="border-top border-secondary pt-2 text-muted small mb-1">Payload Content Body:</div>
                <pre class="text-light bg-black p-2 rounded" style="white-space: pre-wrap; max-height: 200px; overflow-y: auto;">${escapeHtml(respBody)}</pre>
            </div>
        `;
    }, 1200);
}

// ==========================================
// 2. MODULE 1: DNS RECURSIVE & ITERATIVE QUERY RESOLVER
// ==========================================
function initDnsSimulator() {
    const resolveBtn = document.getElementById('dns-resolve-btn');
    if (!resolveBtn) return;

    resolveBtn.addEventListener('click', runDnsSimulation);
}

function runDnsSimulation() {
    const domain = document.getElementById('dns-domain').value.trim();
    const mode = document.getElementById('dns-mode').value;
    const qType = document.getElementById('dns-qtype').value;
    const animBox = document.getElementById('dns-anim-box');
    const resultBox = document.getElementById('dns-result-box');

    if (!domain) {
        alert('Please enter a domain name (e.g., www.vjcet.ac.in).');
        return;
    }

    animBox.innerHTML = '';
    resultBox.innerHTML = '';

    const steps = mode === 'recursive' ? [
        { title: "Step 1: Local DNS Cache Lookup", desc: `Host checks local resolver cache & /etc/hosts for "${domain}". Cache miss.`, icon: "hdd-network", color: "warning" },
        { title: "Step 2: Recursive Query to Local DNS Server", desc: `Client queries Local ISP DNS (192.168.1.1 / 8.8.8.8) with Recursion Desired (RD=1).`, icon: "arrow-right-circle", color: "primary" },
        { title: "Step 3: Root Name Server Query (.)", desc: `Local DNS queries Root Server (a.root-servers.net). Root returns NS referrals for Top-Level Domain (.in / .com).`, icon: "globe", color: "info" },
        { title: "Step 4: TLD Name Server Query (.in)", desc: `Local DNS queries TLD Server (ns1.registry.in). TLD returns Authoritative Name Server for vjcet.ac.in (ns1.vjcet.ac.in).`, icon: "diagram-3", color: "info" },
        { title: "Step 5: Authoritative Name Server Query", desc: `Local DNS queries ns1.vjcet.ac.in for ${qType} record of "${domain}". Authoritative server returns IP 14.139.185.12.`, icon: "shield-check", color: "success" },
        { title: "Step 6: Response Returned & Cached", desc: `Local DNS returns IP to Host and caches mapping with TTL = 3600 seconds.`, icon: "check-circle-fill", color: "success" }
    ] : [
        { title: "Step 1: Client &rarr; Local DNS", desc: `Host sends Iterative Query to Local DNS Server.`, icon: "hdd-network", color: "warning" },
        { title: "Step 2: Client &rarr; Root Server (.)", desc: `Client contacts Root Server. Root replies: "I don't know the IP, ask the .in TLD Server at 37.209.192.10".`, icon: "globe", color: "info" },
        { title: "Step 3: Client &rarr; TLD Server (.in)", desc: `Client contacts .in TLD Server. TLD replies: "Ask Authoritative Server ns1.vjcet.ac.in at 14.139.185.1".`, icon: "diagram-3", color: "info" },
        { title: "Step 4: Client &rarr; Authoritative Server", desc: `Client queries Authoritative Server directly. ns1.vjcet.ac.in replies: "${domain} is at 14.139.185.12".`, icon: "shield-check", color: "success" }
    ];

    let currentStep = 0;
    const interval = setInterval(() => {
        if (currentStep < steps.length) {
            const s = steps[currentStep];
            const stepEl = document.createElement('div');
            stepEl.className = `alert alert-${s.color} py-2 px-3 mb-2 small shadow-sm animate-fade-in`;
            stepEl.innerHTML = `
                <div class="d-flex align-items-center gap-2">
                    <i class="bi bi-${s.icon} fs-5"></i>
                    <div>
                        <strong>${s.title}</strong>
                        <div class="text-muted mt-1">${s.desc}</div>
                    </div>
                </div>
            `;
            animBox.appendChild(stepEl);
            currentStep++;
        } else {
            clearInterval(interval);
            resultBox.innerHTML = `
                <div class="card bg-success bg-opacity-10 border border-success p-3 rounded-3 mt-3">
                    <h6 class="fw-bold text-success mb-2"><i class="bi bi-check2-all"></i> DNS Resolution Complete (${mode.toUpperCase()} MODE)</h6>
                    <div class="font-mono small">
                        <div><strong>Query Domain:</strong> ${domain}</div>
                        <div><strong>Record Type:</strong> ${qType}</div>
                        <div><strong>Resolved IP Address:</strong> <span class="badge bg-success fs-6">14.139.185.12</span></div>
                        <div><strong>Canonical Name (CNAME):</strong> vjcet.ac.in</div>
                        <div><strong>Authoritative DNS:</strong> ns1.vjcet.ac.in, ns2.vjcet.ac.in</div>
                        <div><strong>TTL (Time-To-Live):</strong> 3600 seconds</div>
                    </div>
                </div>
            `;
        }
    }, 500);
}

// ==========================================
// 3. MODULE 1: BITTORRENT P2P SWARM SIMULATOR
// ==========================================
let swarmInterval = null;
function initBitTorrentSimulator() {
    const startBtn = document.getElementById('bt-start-btn');
    const resetBtn = document.getElementById('bt-reset-btn');
    if (!startBtn) return;

    startBtn.addEventListener('click', toggleBtSwarm);
    resetBtn.addEventListener('click', resetBtSwarm);
    renderBtGrid();
}

const btPeers = [
    { name: "Peer A (Seeder)", speed: 5.2, pieces: 16, state: "Seeding", unchoked: true },
    { name: "Peer B (Leecher)", speed: 2.1, pieces: 6, state: "Downloading", unchoked: true },
    { name: "Peer C (Leecher)", speed: 3.4, pieces: 10, state: "Downloading", unchoked: true },
    { name: "Peer D (Leecher)", speed: 1.8, pieces: 4, state: "Downloading", unchoked: true },
    { name: "Peer E (Leecher)", speed: 0.8, pieces: 2, state: "Choked", unchoked: false },
    { name: "Peer F (Optimistic)", speed: 1.2, pieces: 3, state: "Optimistic Unchoke", unchoked: true }
];

function renderBtGrid() {
    const container = document.getElementById('bt-swarm-container');
    if (!container) return;

    container.innerHTML = btPeers.map((p, idx) => `
        <div class="col-md-6 col-lg-4">
            <div class="card p-3 border rounded-3 bg-surface shadow-sm h-100">
                <div class="d-flex justify-content-between align-items-center mb-2">
                    <strong class="small">${p.name}</strong>
                    <span class="badge ${p.unchoked ? 'bg-success' : 'bg-secondary'}">${p.state}</span>
                </div>
                <div class="progress mb-2" style="height: 10px;">
                    <div class="progress-bar ${p.pieces === 16 ? 'bg-success' : 'bg-primary'} progress-bar-striped ${p.unchoked && p.pieces < 16 ? 'progress-bar-animated' : ''}" style="width: ${(p.pieces / 16) * 100}%"></div>
                </div>
                <div class="d-flex justify-content-between small text-muted">
                    <span>Pieces: ${p.pieces}/16 (${Math.round((p.pieces/16)*100)}%)</span>
                    <span><i class="bi bi-speedometer2"></i> ${p.unchoked ? p.speed : 0} MB/s</span>
                </div>
            </div>
        </div>
    `).join('');
}

function toggleBtSwarm() {
    const btn = document.getElementById('bt-start-btn');
    if (swarmInterval) {
        clearInterval(swarmInterval);
        swarmInterval = null;
        btn.innerHTML = '<i class="bi bi-play-fill"></i> Resume Swarm Simulation';
        btn.className = 'btn btn-primary btn-sm';
    } else {
        btn.innerHTML = '<i class="bi bi-pause-fill"></i> Pause Swarm';
        btn.className = 'btn btn-warning btn-sm';
        swarmInterval = setInterval(() => {
            btPeers.forEach(p => {
                if (p.unchoked && p.pieces < 16) {
                    p.pieces += 1;
                    if (p.pieces >= 16) {
                        p.state = "Seeding";
                        p.pieces = 16;
                    }
                }
            });
            renderBtGrid();
            if (btPeers.every(p => p.pieces >= 16)) {
                clearInterval(swarmInterval);
                swarmInterval = null;
                btn.innerHTML = '<i class="bi bi-check2-circle"></i> Swarm Completed (100% Seeded)';
                btn.className = 'btn btn-success btn-sm disabled';
            }
        }, 1000);
    }
}

function resetBtSwarm() {
    if (swarmInterval) clearInterval(swarmInterval);
    swarmInterval = null;
    btPeers[0].pieces = 16;
    btPeers[1].pieces = 6;
    btPeers[2].pieces = 10;
    btPeers[3].pieces = 4;
    btPeers[4].pieces = 2;
    btPeers[5].pieces = 3;
    const btn = document.getElementById('bt-start-btn');
    btn.innerHTML = '<i class="bi bi-play-fill"></i> Start Tit-for-Tat Swarm';
    btn.className = 'btn btn-primary btn-sm';
    renderBtGrid();
}

// ==========================================
// 4. MODULE 2: TCP 3-WAY HANDSHAKE & TEARDOWN
// ==========================================
let tcpStep = 0;
const tcpEvents = [
    { sender: "Client", receiver: "Server", flag: "SYN", seq: 1000, ack: 0, desc: "Step 1: Client sends SYN packet to initiate connection. Transitions to SYN_SENT.", clientState: "SYN_SENT", serverState: "LISTEN" },
    { sender: "Server", receiver: "Client", flag: "SYN + ACK", seq: 5000, ack: 1001, desc: "Step 2: Server responds with SYN-ACK (acknowledging Client Seq + 1). Transitions to SYN_RCVD.", clientState: "SYN_SENT", serverState: "SYN_RCVD" },
    { sender: "Client", receiver: "Server", flag: "ACK", seq: 1001, ack: 5001, desc: "Step 3: Client sends final ACK. Handshake complete! Both enter ESTABLISHED state.", clientState: "ESTABLISHED", serverState: "ESTABLISHED" },
    { sender: "Client", receiver: "Server", flag: "PSH + ACK (Data: 512B)", seq: 1001, ack: 5001, desc: "Step 4: Bi-directional application data transfer occurs over full-duplex TCP stream.", clientState: "ESTABLISHED", serverState: "ESTABLISHED" },
    { sender: "Client", receiver: "Server", flag: "FIN + ACK", seq: 1513, ack: 5001, desc: "Step 5: Client initiates graceful teardown. Sends FIN-ACK. Enters FIN_WAIT_1.", clientState: "FIN_WAIT_1", serverState: "CLOSE_WAIT" },
    { sender: "Server", receiver: "Client", flag: "ACK", seq: 5001, ack: 1514, desc: "Step 6: Server sends ACK for FIN. Client enters FIN_WAIT_2.", clientState: "FIN_WAIT_2", serverState: "CLOSE_WAIT" },
    { sender: "Server", receiver: "Client", flag: "FIN + ACK", seq: 5001, ack: 1514, desc: "Step 7: Server closes its send side. Sends FIN-ACK. Enters LAST_ACK.", clientState: "TIME_WAIT (2MSL)", serverState: "LAST_ACK" },
    { sender: "Client", receiver: "Server", flag: "ACK", seq: 1514, ack: 5002, desc: "Step 8: Client sends ACK. Server CLOSED. Client waits 2MSL timer then CLOSED.", clientState: "CLOSED", serverState: "CLOSED" }
];

function initTcpHandshakeSimulator() {
    const stepBtn = document.getElementById('tcp-step-btn');
    const resetBtn = document.getElementById('tcp-reset-btn');
    if (!stepBtn) return;

    stepBtn.addEventListener('click', stepTcpSimulation);
    resetBtn.addEventListener('click', resetTcpSimulation);
}

function stepTcpSimulation() {
    if (tcpStep >= tcpEvents.length) return;

    const ev = tcpEvents[tcpStep];
    const logBox = document.getElementById('tcp-log-box');
    const clientBadge = document.getElementById('tcp-client-state');
    const serverBadge = document.getElementById('tcp-server-state');
    const packetAnim = document.getElementById('tcp-packet-anim');

    clientBadge.innerText = ev.clientState;
    serverBadge.innerText = ev.serverState;

    // Render Packet Animation
    const isClientSender = ev.sender === "Client";
    packetAnim.innerHTML = `
        <div class="d-flex align-items-center justify-content-between p-2 rounded bg-dark text-white font-mono small animate-fade-in mb-2">
            <span class="badge ${isClientSender ? 'bg-primary' : 'bg-success'}">${ev.sender} &rarr; ${ev.receiver}</span>
            <span class="text-warning fw-bold">[${ev.flag}]</span>
            <span>Seq=${ev.seq} | Ack=${ev.ack}</span>
        </div>
    `;

    // Append to Log
    const entry = document.createElement('div');
    entry.className = `alert alert-${isClientSender ? 'primary' : 'success'} py-2 px-3 small mb-2`;
    entry.innerHTML = `<strong>${ev.desc}</strong><div class="font-mono mt-1 text-muted">Flags: [${ev.flag}], Sequence Number: ${ev.seq}, Acknowledgement Number: ${ev.ack}</div>`;
    logBox.appendChild(entry);
    logBox.scrollTop = logBox.scrollHeight;

    tcpStep++;

    const stepBtn = document.getElementById('tcp-step-btn');
    if (tcpStep >= tcpEvents.length) {
        stepBtn.innerHTML = '<i class="bi bi-check-all"></i> Simulation Finished';
        stepBtn.classList.add('disabled');
    } else {
        stepBtn.innerHTML = `<i class="bi bi-play-fill"></i> Next Step (${tcpStep + 1}/${tcpEvents.length})`;
    }
}

function resetTcpSimulation() {
    tcpStep = 0;
    document.getElementById('tcp-log-box').innerHTML = '';
    document.getElementById('tcp-packet-anim').innerHTML = '<div class="text-muted text-center py-2 small">Press "Next Step" to start TCP Handshake</div>';
    document.getElementById('tcp-client-state').innerText = 'CLOSED';
    document.getElementById('tcp-server-state').innerText = 'LISTEN';
    const stepBtn = document.getElementById('tcp-step-btn');
    stepBtn.innerHTML = '<i class="bi bi-play-fill"></i> Start Handshake (Step 1)';
    stepBtn.classList.remove('disabled');
}

// ==========================================
// 5. MODULE 2: TCP CONGESTION CONTROL (AIMD / RENO)
// ==========================================
let cwndChart = null;
let cwndData = [];
let currentRtt = 0;
let currentCwnd = 1;
let ssthresh = 16;
let congestionState = "Slow Start"; // "Slow Start", "Congestion Avoidance", "Fast Recovery"

function initTcpCongestionSimulator() {
    const canvas = document.getElementById('tcp-cwnd-canvas');
    if (!canvas) return;

    resetTcpCongestion();
    document.getElementById('btn-cwnd-step')?.addEventListener('click', stepCwnd);
    document.getElementById('btn-cwnd-3dup')?.addEventListener('click', trigger3DupAck);
    document.getElementById('btn-cwnd-timeout')?.addEventListener('click', triggerTimeout);
    document.getElementById('btn-cwnd-reset')?.addEventListener('click', resetTcpCongestion);
}

function resetTcpCongestion() {
    currentRtt = 0;
    currentCwnd = 1;
    ssthresh = 16;
    congestionState = "Slow Start";
    cwndData = [{ rtt: 0, cwnd: 1, ssthresh: 16, state: "Slow Start" }];
    updateCwndUI();
    drawCwndChart();
}

function stepCwnd() {
    currentRtt++;
    if (congestionState === "Slow Start") {
        currentCwnd = currentCwnd * 2;
        if (currentCwnd >= ssthresh) {
            currentCwnd = ssthresh;
            congestionState = "Congestion Avoidance";
        }
    } else if (congestionState === "Congestion Avoidance") {
        currentCwnd += 1; // Linear additive increase (+1 MSS per RTT)
    } else if (congestionState === "Fast Recovery") {
        currentCwnd = ssthresh;
        congestionState = "Congestion Avoidance";
    }

    cwndData.push({ rtt: currentRtt, cwnd: currentCwnd, ssthresh: ssthresh, state: congestionState });
    updateCwndUI();
    drawCwndChart();
}

function trigger3DupAck() {
    currentRtt++;
    ssthresh = Math.max(2, Math.floor(currentCwnd / 2));
    currentCwnd = ssthresh + 3; // Fast Retransmit / Fast Recovery
    congestionState = "Fast Recovery";
    cwndData.push({ rtt: currentRtt, cwnd: currentCwnd, ssthresh: ssthresh, state: "3 Dup ACKs (Fast Retransmit)" });
    updateCwndUI();
    drawCwndChart();
}

function triggerTimeout() {
    currentRtt++;
    ssthresh = Math.max(2, Math.floor(currentCwnd / 2));
    currentCwnd = 1; // Reno/Tahoe timeout drops cwnd to 1 MSS
    congestionState = "Slow Start";
    cwndData.push({ rtt: currentRtt, cwnd: currentCwnd, ssthresh: ssthresh, state: "Timeout (Loss Detected)" });
    updateCwndUI();
    drawCwndChart();
}

function updateCwndUI() {
    document.getElementById('val-current-cwnd').innerText = `${currentCwnd} MSS`;
    document.getElementById('val-current-ssthresh').innerText = `${ssthresh} MSS`;
    document.getElementById('val-current-rtt').innerText = `Round ${currentRtt}`;
    const badge = document.getElementById('val-current-phase');
    badge.innerText = congestionState;
    if (congestionState === "Slow Start") badge.className = 'badge bg-primary';
    else if (congestionState === "Congestion Avoidance") badge.className = 'badge bg-info';
    else badge.className = 'badge bg-danger';
}

function drawCwndChart() {
    const canvas = document.getElementById('tcp-cwnd-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.parentElement.clientWidth || 600;
    const height = canvas.height = 260;

    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const bgGrid = isDark ? '#1e293b' : '#f1f5f9';
    const textColor = isDark ? '#94a3b8' : '#64748b';
    const lineColor = '#3b82f6';
    const threshColor = '#ef4444';

    ctx.clearRect(0, 0, width, height);

    // Padding
    const pLeft = 45, pRight = 20, pTop = 20, pBottom = 35;
    const gWidth = width - pLeft - pRight;
    const gHeight = height - pTop - pBottom;

    // Draw Grid Lines
    ctx.strokeStyle = bgGrid;
    ctx.lineWidth = 1;
    ctx.fillStyle = textColor;
    ctx.font = '10px Inter, sans-serif';

    const maxCwnd = Math.max(32, ...cwndData.map(d => Math.max(d.cwnd, d.ssthresh))) + 4;
    const maxRtt = Math.max(15, currentRtt + 2);

    // Y Axis Grid
    for (let yVal = 0; yVal <= maxCwnd; yVal += 8) {
        const y = pTop + gHeight - (yVal / maxCwnd) * gHeight;
        ctx.beginPath();
        ctx.moveTo(pLeft, y);
        ctx.lineTo(width - pRight, y);
        ctx.stroke();
        ctx.fillText(`${yVal}`, 15, y + 4);
    }

    // X Axis Grid
    for (let r = 0; r <= maxRtt; r += 2) {
        const x = pLeft + (r / maxRtt) * gWidth;
        ctx.beginPath();
        ctx.moveTo(x, pTop);
        ctx.lineTo(x, height - pBottom);
        ctx.stroke();
        ctx.fillText(`R${r}`, x - 8, height - 12);
    }

    // Draw ssthresh threshold line
    ctx.strokeStyle = threshColor;
    ctx.setLineDash([4, 4]);
    ctx.lineWidth = 2;
    const yThresh = pTop + gHeight - (ssthresh / maxCwnd) * gHeight;
    ctx.beginPath();
    ctx.moveTo(pLeft, yThresh);
    ctx.lineTo(width - pRight, yThresh);
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = threshColor;
    ctx.fillText(`ssthresh = ${ssthresh}`, width - pRight - 80, yThresh - 6);

    // Draw cwnd line & markers
    ctx.strokeStyle = lineColor;
    ctx.lineWidth = 3;
    ctx.beginPath();
    cwndData.forEach((d, i) => {
        const x = pLeft + (d.rtt / maxRtt) * gWidth;
        const y = pTop + gHeight - (d.cwnd / maxCwnd) * gHeight;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
    });
    ctx.stroke();

    // Draw points
    cwndData.forEach(d => {
        const x = pLeft + (d.rtt / maxRtt) * gWidth;
        const y = pTop + gHeight - (d.cwnd / maxCwnd) * gHeight;
        ctx.fillStyle = d.state.includes('Loss') ? '#ef4444' : (d.state.includes('Fast') ? '#f59e0b' : '#3b82f6');
        ctx.beginPath();
        ctx.arc(x, y, 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 1.5;
        ctx.stroke();
    });
}

// ==========================================
// 6. MODULE 2: IPV4 SUBNET CALCULATOR
// ==========================================
function initSubnetSimulator() {
    const btn = document.getElementById('sim-calc-subnet');
    if (!btn) return;
    btn.addEventListener('click', () => {
        const ip = document.getElementById('sim-subnet-ip').value.trim();
        const prefix = parseInt(document.getElementById('sim-subnet-prefix').value);
        const resBox = document.getElementById('sim-subnet-result');

        if (!ip || isNaN(prefix) || prefix < 0 || prefix > 32) {
            alert('Please enter valid IPv4 address and CIDR prefix (0-32).');
            return;
        }

        const octets = ip.split('.').map(Number);
        if (octets.length !== 4 || octets.some(o => isNaN(o) || o < 0 || o > 255)) {
            alert('Invalid IPv4 address.');
            return;
        }

        const ipInt = (octets[0] << 24) | (octets[1] << 16) | (octets[2] << 8) | octets[3];
        const maskInt = prefix === 0 ? 0 : (~0 << (32 - prefix)) >>> 0;
        const netInt = (ipInt & maskInt) >>> 0;
        const wildInt = (~maskInt) >>> 0;
        const bcastInt = (netInt | wildInt) >>> 0;

        const toIp = val => [(val >>> 24) & 255, (val >>> 16) & 255, (val >>> 8) & 255, val & 255].join('.');
        const totalHosts = Math.pow(2, 32 - prefix);
        const usableHosts = prefix >= 31 ? (prefix === 31 ? 2 : 1) : totalHosts - 2;

        resBox.innerHTML = `
            <div class="card p-3 bg-surface border rounded-3 small font-mono">
                <div class="row g-2">
                    <div class="col-md-6"><strong>Network Address (ID):</strong> <span class="text-primary fw-bold">${toIp(netInt)}/${prefix}</span></div>
                    <div class="col-md-6"><strong>Broadcast Address:</strong> <span class="text-danger fw-bold">${toIp(bcastInt)}</span></div>
                    <div class="col-md-6"><strong>Subnet Mask:</strong> ${toIp(maskInt)}</div>
                    <div class="col-md-6"><strong>Wildcard Mask:</strong> ${toIp(wildInt)}</div>
                    <div class="col-md-6"><strong>First Usable Host:</strong> ${toIp(netInt + 1)}</div>
                    <div class="col-md-6"><strong>Last Usable Host:</strong> ${toIp(bcastInt - 1)}</div>
                    <div class="col-md-6"><strong>Total Host Addresses:</strong> ${totalHosts.toLocaleString()}</div>
                    <div class="col-md-6"><strong>Usable Hosts:</strong> <span class="badge bg-success">${usableHosts.toLocaleString()}</span></div>
                </div>
            </div>
        `;
    });
}

// ==========================================
// 7. MODULE 2: DIJKSTRA SHORTEST PATH ROUTING (OSPF)
// ==========================================
const dijkstraGraph = {
    A: { B: 4, C: 2 },
    B: { A: 4, C: 1, D: 5 },
    C: { A: 2, B: 1, D: 8, E: 10 },
    D: { B: 5, C: 8, E: 2, F: 6 },
    E: { C: 10, D: 2, F: 3 },
    F: { D: 6, E: 3 }
};

function initDijkstraSimulator() {
    const runBtn = document.getElementById('dijkstra-run-btn');
    if (!runBtn) return;
    runBtn.addEventListener('click', runDijkstraSimulation);
    drawDijkstraGraph({});
}

function runDijkstraSimulation() {
    const src = document.getElementById('dijkstra-src').value;
    const dest = document.getElementById('dijkstra-dest').value;
    const resultBox = document.getElementById('dijkstra-result-box');

    const nodes = Object.keys(dijkstraGraph);
    const dist = {};
    const prev = {};
    const unvisited = new Set(nodes);

    nodes.forEach(n => {
        dist[n] = Infinity;
        prev[n] = null;
    });
    dist[src] = 0;

    const stepsLog = [];

    while (unvisited.size > 0) {
        let curr = null;
        let minD = Infinity;
        unvisited.forEach(n => {
            if (dist[n] < minD) {
                minD = dist[n];
                curr = n;
            }
        });

        if (curr === null || dist[curr] === Infinity) break;
        unvisited.delete(curr);

        stepsLog.push(`Visiting Node ${curr} (Current Min Cost: ${dist[curr]})`);

        for (const neighbor in dijkstraGraph[curr]) {
            if (unvisited.has(neighbor)) {
                const alt = dist[curr] + dijkstraGraph[curr][neighbor];
                if (alt < dist[neighbor]) {
                    dist[neighbor] = alt;
                    prev[neighbor] = curr;
                    stepsLog.push(` &rarr; Relax edge (${curr}&rarr;${neighbor}): Updated dist[${neighbor}] = ${alt}`);
                }
            }
        }
    }

    // Reconstruct Path
    const path = [];
    let u = dest;
    while (u !== null) {
        path.unshift(u);
        u = prev[u];
    }

    resultBox.innerHTML = `
        <div class="alert alert-success small mb-2">
            <strong>Optimal Shortest Path from ${src} to ${dest}:</strong>
            <div class="fs-5 fw-bold text-success my-1">${path.join(' &rarr; ')}</div>
            <div><strong>Total Cumulative Link Metric / Cost:</strong> <span class="badge bg-success fs-6">${dist[dest]}</span></div>
        </div>
        <div class="card p-2 bg-surface border rounded-3 small font-mono" style="max-height: 120px; overflow-y: auto;">
            <strong>Step-by-Step Relaxation Trace:</strong>
            ${stepsLog.map(s => `<div>${s}</div>`).join('')}
        </div>
    `;

    drawDijkstraGraph(prev, path);
}

function drawDijkstraGraph(prev, optimalPath = []) {
    const canvas = document.getElementById('dijkstra-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.parentElement.clientWidth || 550;
    const height = canvas.height = 240;

    const coords = {
        A: { x: 70, y: 120 },
        B: { x: 190, y: 50 },
        C: { x: 190, y: 190 },
        D: { x: 360, y: 50 },
        E: { x: 360, y: 190 },
        F: { x: 480, y: 120 }
    };

    ctx.clearRect(0, 0, width, height);

    // Draw Links
    for (const u in dijkstraGraph) {
        for (const v in dijkstraGraph[u]) {
            if (u < v) { // draw once
                const isOptimalEdge = optimalPath.some((node, idx) => 
                    (node === u && optimalPath[idx+1] === v) || (node === v && optimalPath[idx+1] === u)
                );

                ctx.beginPath();
                ctx.moveTo(coords[u].x, coords[u].y);
                ctx.lineTo(coords[v].x, coords[v].y);
                ctx.strokeStyle = isOptimalEdge ? '#10b981' : '#94a3b8';
                ctx.lineWidth = isOptimalEdge ? 4 : 1.5;
                ctx.stroke();

                // Draw edge cost label
                const midX = (coords[u].x + coords[v].x) / 2;
                const midY = (coords[u].y + coords[v].y) / 2;
                ctx.fillStyle = isOptimalEdge ? '#059669' : '#64748b';
                ctx.font = 'bold 11px Inter, sans-serif';
                ctx.fillText(`${dijkstraGraph[u][v]}`, midX + 3, midY - 3);
            }
        }
    }

    // Draw Nodes
    for (const n in coords) {
        const inPath = optimalPath.includes(n);
        ctx.beginPath();
        ctx.arc(coords[n].x, coords[n].y, 18, 0, 2 * Math.PI);
        ctx.fillStyle = inPath ? '#10b981' : '#1e3a8a';
        ctx.fill();
        ctx.strokeStyle = '#ffffff';
        ctx.lineWidth = 2;
        ctx.stroke();

        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 13px Outfit, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(n, coords[n].x, coords[n].y);
    }
}

// ==========================================
// 8. MODULE 2: DISTANCE VECTOR ROUTING (RIP)
// ==========================================
function initDistanceVectorSimulator() {
    const btn = document.getElementById('dv-converge-btn');
    if (!btn) return;
    btn.addEventListener('click', runDistanceVectorSimulation);
}

function runDistanceVectorSimulation() {
    const box = document.getElementById('dv-tables-box');
    box.innerHTML = `
        <div class="row g-3 small">
            <div class="col-md-6">
                <div class="card p-2 border">
                    <strong class="text-primary mb-1">Router R1 Routing Table</strong>
                    <table class="table table-sm table-bordered text-center mb-0">
                        <thead class="table-light"><tr><th>Dest</th><th>Cost</th><th>Next Hop</th></tr></thead>
                        <tbody>
                            <tr><td>R1</td><td>0</td><td>-</td></tr>
                            <tr><td>R2</td><td>1</td><td>R2</td></tr>
                            <tr><td>R3</td><td>3</td><td>R2</td></tr>
                            <tr><td>R4</td><td>7</td><td>R2</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="col-md-6">
                <div class="card p-2 border">
                    <strong class="text-primary mb-1">Router R2 Routing Table</strong>
                    <table class="table table-sm table-bordered text-center mb-0">
                        <thead class="table-light"><tr><th>Dest</th><th>Cost</th><th>Next Hop</th></tr></thead>
                        <tbody>
                            <tr><td>R1</td><td>1</td><td>R1</td></tr>
                            <tr><td>R2</td><td>0</td><td>-</td></tr>
                            <tr><td>R3</td><td>2</td><td>R3</td></tr>
                            <tr><td>R4</td><td>6</td><td>R3</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div class="alert alert-success mt-2 p-2 small mb-0">
            <i class="bi bi-check-circle-fill"></i> Bellman-Ford equation <code>Dx(y) = min_v { c(x,v) + Dv(y) }</code> converged across all 4 routers in 3 exchange iterations!
        </div>
    `;
}

// ==========================================
// 9. MODULE 3: SLIDING WINDOW PROTOCOLS (ARQ)
// ==========================================
let arqFrames = [];
let nextFrameToSend = 0;
let arqWindowSize = 4;
let arqProtocol = "gbn"; // "saw", "gbn", "sr"

function initSlidingWindowSimulator() {
    const sendBtn = document.getElementById('arq-send-btn');
    const dropBtn = document.getElementById('arq-drop-btn');
    const ackDropBtn = document.getElementById('arq-ackdrop-btn');
    const resetBtn = document.getElementById('arq-reset-btn');
    const protoSel = document.getElementById('arq-protocol-sel');

    if (!sendBtn) return;

    protoSel.addEventListener('change', (e) => {
        arqProtocol = e.target.value;
        arqWindowSize = arqProtocol === "saw" ? 1 : 4;
        resetArqSimulation();
    });

    sendBtn.addEventListener('click', sendArqFrame);
    dropBtn.addEventListener('click', dropArqFrame);
    ackDropBtn.addEventListener('click', dropArqAck);
    resetBtn.addEventListener('click', resetArqSimulation);

    resetArqSimulation();
}

function resetArqSimulation() {
    nextFrameToSend = 0;
    arqFrames = Array.from({ length: 8 }, (_, i) => ({ seq: i, status: "unsent" }));
    document.getElementById('arq-log-box').innerHTML = '';
    renderArqTrack();
}

function renderArqTrack() {
    const container = document.getElementById('arq-window-track');
    if (!container) return;

    container.innerHTML = arqFrames.map(f => {
        let colorClass = 'bg-secondary bg-opacity-25 text-muted';
        let statusText = 'Unsent';
        if (f.status === 'in-flight') { colorClass = 'bg-warning text-dark'; statusText = 'In Flight'; }
        else if (f.status === 'acked') { colorClass = 'bg-success text-white'; statusText = 'ACKed'; }
        else if (f.status === 'dropped') { colorClass = 'bg-danger text-white'; statusText = 'Frame Lost'; }
        else if (f.status === 'ack-dropped') { colorClass = 'bg-danger text-white'; statusText = 'ACK Lost'; }

        return `
            <div class="col-3 col-md-1 text-center">
                <div class="card p-2 border ${colorClass} rounded-3 font-mono">
                    <div class="fw-bold">F${f.seq}</div>
                    <div style="font-size: 10px;">${statusText}</div>
                </div>
            </div>
        `;
    }).join('');
}

function sendArqFrame() {
    if (nextFrameToSend >= arqFrames.length) {
        alert('All 8 frames sent.');
        return;
    }

    const currentSeq = nextFrameToSend;
    arqFrames[currentSeq].status = 'in-flight';
    renderArqTrack();

    logArq(`[Sender &rarr; Receiver] Transmitting Frame F${currentSeq} (Seq=${currentSeq})`, 'primary');

    setTimeout(() => {
        if (arqFrames[currentSeq].status === 'in-flight') {
            arqFrames[currentSeq].status = 'acked';
            renderArqTrack();
            logArq(`[Receiver &rarr; Sender] Received F${currentSeq}. Transmitting ACK ${currentSeq + 1}`, 'success');
        }
    }, 1000);

    nextFrameToSend++;
}

function dropArqFrame() {
    if (nextFrameToSend >= arqFrames.length) return;
    const currentSeq = nextFrameToSend;
    arqFrames[currentSeq].status = 'dropped';
    renderArqTrack();

    logArq(`[Channel Error] Frame F${currentSeq} DROPPED / CORRUPTED in transit!`, 'danger');

    setTimeout(() => {
        logArq(`[Sender Timer] Timeout expired for Frame F${currentSeq}! Retransmitting...`, 'warning');
        if (arqProtocol === 'gbn') {
            logArq(`[Go-Back-N] Resending entire window starting from F${currentSeq}`, 'info');
        } else if (arqProtocol === 'sr') {
            logArq(`[Selective Repeat] Resending only missing Frame F${currentSeq}`, 'info');
        }
    }, 2000);

    nextFrameToSend++;
}

function dropArqAck() {
    if (nextFrameToSend >= arqFrames.length) return;
    const currentSeq = nextFrameToSend;
    arqFrames[currentSeq].status = 'ack-dropped';
    renderArqTrack();

    logArq(`[Sender &rarr; Receiver] Frame F${currentSeq} delivered, but returning ACK was LOST!`, 'danger');

    setTimeout(() => {
        logArq(`[Sender Timeout] Retransmitting F${currentSeq} due to unacknowledged timer.`, 'warning');
    }, 2000);

    nextFrameToSend++;
}

function logArq(msg, type = 'info') {
    const box = document.getElementById('arq-log-box');
    const el = document.createElement('div');
    el.className = `alert alert-${type} py-1 px-2 small mb-1 font-mono`;
    el.innerHTML = msg;
    box.appendChild(el);
    box.scrollTop = box.scrollHeight;
}

// ==========================================
// 10. MODULE 3: CRC GENERATOR & ERROR DETECTOR
// ==========================================
function initCrcSimulator() {
    const btn = document.getElementById('crc-calc-btn');
    const verifyBtn = document.getElementById('crc-verify-btn');
    if (!btn) return;

    btn.addEventListener('click', calculateCrc);
    verifyBtn?.addEventListener('click', verifyCrcReceived);
}

function calculateCrc() {
    const data = document.getElementById('crc-data-input').value.trim();
    const poly = document.getElementById('crc-poly-input').value.trim();
    const resultBox = document.getElementById('crc-sim-result');

    if (!/^[01]+$/.test(data) || !/^[01]+$/.test(poly)) {
        alert('Data and Divisor must contain only binary bits (0 and 1).');
        return;
    }

    const n = poly.length - 1;
    const augmented = data + '0'.repeat(n);
    const { remainder, steps } = modulo2Division(augmented, poly);

    const codeword = data + remainder;

    resultBox.innerHTML = `
        <div class="card p-3 bg-surface border rounded-3 small font-mono mt-3">
            <h6 class="fw-bold text-primary mb-2">Sender Side CRC Generation</h6>
            <div><strong>Augmented Data (Data + ${n} zeros):</strong> ${augmented}</div>
            <div><strong>Generator Polynomial Divisor:</strong> ${poly}</div>
            <div><strong>Calculated Remainder (FCS / CRC Checksum):</strong> <span class="badge bg-warning text-dark fs-6">${remainder}</span></div>
            <div class="mt-2"><strong>Final Transmitted Frame Codeword (Data + CRC):</strong></div>
            <div class="input-group mt-1">
                <input type="text" id="crc-rx-codeword" class="form-control font-mono fw-bold text-success" value="${codeword}">
                <button class="btn btn-outline-danger" id="crc-flip-bit-btn" type="button"><i class="bi bi-radioactive"></i> Flip 1 Bit (Inject Error)</button>
            </div>
            <button class="btn btn-success btn-sm mt-3" id="crc-verify-btn"><i class="bi bi-shield-check"></i> Verify at Receiver Side</button>
            <div id="crc-rx-verification" class="mt-2"></div>
        </div>
    `;

    document.getElementById('crc-flip-bit-btn').addEventListener('click', () => {
        const inp = document.getElementById('crc-rx-codeword');
        const val = inp.value;
        const flipIdx = Math.floor(Math.random() * val.length);
        const flippedChar = val[flipIdx] === '1' ? '0' : '1';
        inp.value = val.substring(0, flipIdx) + flippedChar + val.substring(flipIdx + 1);
        inp.classList.remove('text-success');
        inp.classList.add('text-danger');
    });

    document.getElementById('crc-verify-btn').addEventListener('click', verifyCrcReceived);
}

function verifyCrcReceived() {
    const rxCodeword = document.getElementById('crc-rx-codeword').value.trim();
    const poly = document.getElementById('crc-poly-input').value.trim();
    const outBox = document.getElementById('crc-rx-verification');

    const { remainder } = modulo2Division(rxCodeword, poly);
    const hasError = parseInt(remainder, 2) !== 0;

    outBox.innerHTML = `
        <div class="alert ${hasError ? 'alert-danger' : 'alert-success'} py-2 px-3 small mt-2">
            <strong>Receiver Division Remainder (Syndrome):</strong> <span class="font-mono fw-bold">${remainder}</span>
            <div class="mt-1">${hasError ? '<strong><i class="bi bi-x-circle-fill"></i> ERROR DETECTED!</strong> Non-zero remainder indicates frame was corrupted in transit. Frame discarded.' : '<strong><i class="bi bi-check-circle-fill"></i> NO ERROR DETECTED!</strong> Zero remainder proves frame integrity is verified. Accepted.'}</div>
        </div>
    `;
}

function modulo2Division(dividend, divisor) {
    let cur = dividend.substring(0, divisor.length);
    let steps = [];

    for (let i = divisor.length; i <= dividend.length; i++) {
        if (cur[0] === '1') {
            let res = '';
            for (let j = 0; j < divisor.length; j++) {
                res += (cur[j] === divisor[j]) ? '0' : '1';
            }
            cur = res.substring(1) + (i < dividend.length ? dividend[i] : '');
        } else {
            cur = cur.substring(1) + (i < dividend.length ? dividend[i] : '');
        }
    }

    return { remainder: cur, steps };
}

// ==========================================
// 11. MODULE 3: HAMMING (7,4) ERROR CORRECTOR
// ==========================================
function initHammingSimulator() {
    const btn = document.getElementById('hamming-gen-btn');
    if (!btn) return;
    btn.addEventListener('click', generateHammingCode);
}

function generateHammingCode() {
    const d3 = parseInt(document.getElementById('ham-d3').value);
    const d2 = parseInt(document.getElementById('ham-d2').value);
    const d1 = parseInt(document.getElementById('ham-d1').value);
    const d0 = parseInt(document.getElementById('ham-d0').value);

    // Hamming (7,4) Parity equations (Even Parity)
    // Bit layout: [p1, p2, d0, p3, d1, d2, d3]
    // p1 covers bits 1, 3, 5, 7 -> p1 ^ d0 ^ d1 ^ d3 = 0 => p1 = d0 ^ d1 ^ d3
    // p2 covers bits 2, 3, 6, 7 -> p2 ^ d0 ^ d2 ^ d3 = 0 => p2 = d0 ^ d2 ^ d3
    // p3 covers bits 4, 5, 6, 7 -> p3 ^ d1 ^ d2 ^ d3 = 0 => p3 = d1 ^ d2 ^ d3

    const p1 = d0 ^ d1 ^ d3;
    const p2 = d0 ^ d2 ^ d3;
    const p3 = d1 ^ d2 ^ d3;

    const codeword = [p1, p2, d0, p3, d1, d2, d3];

    const box = document.getElementById('hamming-result-box');
    box.innerHTML = `
        <div class="card p-3 bg-surface border rounded-3 small font-mono mt-3">
            <h6 class="fw-bold text-primary mb-2">Hamming (7,4) Codeword Generated</h6>
            <div class="d-flex flex-wrap gap-2 mb-3">
                ${codeword.map((b, idx) => `
                    <button class="btn btn-outline-primary btn-sm ham-bit-btn" data-index="${idx}" data-val="${b}">
                        <span style="font-size: 10px;" class="d-block text-muted">Bit ${idx + 1} (${idx === 0 ? 'P1' : idx === 1 ? 'P2' : idx === 2 ? 'D0' : idx === 3 ? 'P3' : idx === 4 ? 'D1' : idx === 5 ? 'D2' : 'D3'})</span>
                        <strong>${b}</strong>
                    </button>
                `).join('')}
            </div>
            <div class="text-muted small mb-2"><i class="bi bi-info-circle"></i> Click on any bit above to inject a bit flip error!</div>
            <button class="btn btn-success btn-sm" id="ham-syndrome-btn"><i class="bi bi-cpu"></i> Calculate Syndrome &amp; Auto-Correct</button>
            <div id="ham-syndrome-out" class="mt-2"></div>
        </div>
    `;

    const bitBtns = box.querySelectorAll('.ham-bit-btn');
    bitBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const currentVal = parseInt(btn.getAttribute('data-val'));
            const newVal = currentVal === 1 ? 0 : 1;
            btn.setAttribute('data-val', newVal);
            btn.querySelector('strong').innerText = newVal;
            btn.classList.toggle('btn-outline-primary');
            btn.classList.toggle('btn-danger');
        });
    });

    document.getElementById('ham-syndrome-btn').addEventListener('click', () => {
        const currentBits = Array.from(box.querySelectorAll('.ham-bit-btn')).map(b => parseInt(b.getAttribute('data-val')));
        // Bits: b1=p1, b2=p2, b3=d0, b4=p3, b5=d1, b6=d2, b7=d3
        const s1 = currentBits[0] ^ currentBits[2] ^ currentBits[4] ^ currentBits[6];
        const s2 = currentBits[1] ^ currentBits[2] ^ currentBits[5] ^ currentBits[6];
        const s3 = currentBits[3] ^ currentBits[4] ^ currentBits[5] ^ currentBits[6];

        const syndromeVal = (s3 << 2) | (s2 << 1) | s1; // Decimal error location

        const out = document.getElementById('ham-syndrome-out');
        if (syndromeVal === 0) {
            out.innerHTML = `<div class="alert alert-success py-2 px-3 small"><strong><i class="bi bi-check-circle-fill"></i> Syndrome S = (0,0,0): No Error Detected!</strong> Received codeword is valid.</div>`;
        } else {
            out.innerHTML = `
                <div class="alert alert-danger py-2 px-3 small">
                    <strong><i class="bi bi-exclamation-triangle-fill"></i> Single Bit Error Detected at Position ${syndromeVal}!</strong>
                    <div>Syndrome bits: S3=${s3}, S2=${s2}, S1=${s1} &rarr; Binary ${s3}${s2}${s1} = Decimal ${syndromeVal}</div>
                    <div class="mt-1 text-success fw-bold">&rarr; Auto-Correcting Bit ${syndromeVal}: Flipped ${currentBits[syndromeVal - 1]} back to ${currentBits[syndromeVal - 1] === 1 ? 0 : 1}</div>
                </div>
            `;
        }
    });
}

// ==========================================
// 12. MODULE 3: CSMA/CD & CSMA/CA SIMULATOR
// ==========================================
function initCsmaSimulator() {
    const transmitBtn = document.getElementById('csma-transmit-btn');
    if (!transmitBtn) return;
    transmitBtn.addEventListener('click', runCsmaSimulation);
}

function runCsmaSimulation() {
    const stCount = parseInt(document.getElementById('csma-stations').value);
    const box = document.getElementById('csma-log-box');
    box.innerHTML = '';

    const log = (msg, color = 'info') => {
        const div = document.createElement('div');
        div.className = `alert alert-${color} py-1 px-2 small mb-1 font-mono`;
        div.innerHTML = msg;
        box.appendChild(div);
        box.scrollTop = box.scrollHeight;
    };

    log(`[Medium Sensing] Stations 1 through ${stCount} sensing carrier line (1-persistent CSMA)...`, 'info');

    setTimeout(() => {
        if (stCount > 1) {
            log(`[COLLISION DETECTED!] Multiple stations transmitted simultaneously on bus wire!`, 'danger');
            log(`[Jam Signal] Transmitting 48-bit Jam Signal to enforce collision state.`, 'warning');
            const k = Math.floor(Math.random() * 4);
            log(`[Exponential Backoff] Station 1 chose K = ${k}, Waiting ${k} &times; 51.2 &micro;s slot time before retry.`, 'secondary');
            setTimeout(() => {
                log(`[Retransmission Success] Line clear. Station 1 successfully transmitted frame without collision.`, 'success');
            }, 1200);
        } else {
            log(`[Channel Idle] Station 1 captured line. Frame transmitted successfully without collision.`, 'success');
        }
    }, 800);
}

// ==========================================
// 13. MODULE 4: LINE CODING WAVEFORM GENERATOR
// ==========================================
function initLineCodingSimulator() {
    const canvas = document.getElementById('line-code-canvas');
    const btn = document.getElementById('btn-render-waveforms');
    if (!canvas || !btn) return;

    btn.addEventListener('click', drawLineCodeWaveforms);
    drawLineCodeWaveforms();
}

function drawLineCodeWaveforms() {
    const canvas = document.getElementById('line-code-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width = canvas.parentElement.clientWidth || 650;
    const height = canvas.height = 360;

    const bits = (document.getElementById('input-linecode-bits')?.value || '10110001').trim();
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';

    ctx.clearRect(0, 0, width, height);

    const schemes = ['Unipolar NRZ', 'Polar NRZ-L', 'Polar NRZ-I', 'Manchester', 'Differential Manchester', 'AMI'];
    const pLeft = 140, pRight = 20, pTop = 30;
    const bitWidth = (width - pLeft - pRight) / bits.length;
    const rowHeight = 45;

    // Draw Bit Headers
    ctx.fillStyle = isDark ? '#f8fafc' : '#0f172a';
    ctx.font = 'bold 12px monospace';
    for (let i = 0; i < bits.length; i++) {
        const x = pLeft + i * bitWidth + bitWidth / 2;
        ctx.fillText(bits[i], x - 4, 18);
        // Vertical dashed lines
        ctx.strokeStyle = isDark ? '#334155' : '#e2e8f0';
        ctx.setLineDash([2, 4]);
        ctx.beginPath();
        ctx.moveTo(pLeft + i * bitWidth, 25);
        ctx.lineTo(pLeft + i * bitWidth, height - 10);
        ctx.stroke();
    }
    ctx.setLineDash([]);

    // Draw each scheme
    schemes.forEach((scheme, rowIdx) => {
        const baseY = pTop + rowIdx * rowHeight + rowHeight / 2;

        // Label
        ctx.fillStyle = isDark ? '#94a3b8' : '#475569';
        ctx.font = '11px Inter, sans-serif';
        ctx.fillText(scheme, 10, baseY + 4);

        // Center line
        ctx.strokeStyle = isDark ? '#1e293b' : '#f1f5f9';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(pLeft, baseY);
        ctx.lineTo(width - pRight, baseY);
        ctx.stroke();

        // Waveform
        ctx.strokeStyle = '#3b82f6';
        ctx.lineWidth = 2.5;
        ctx.beginPath();

        let lastLevel = 1;
        let amiSign = 1;

        for (let i = 0; i < bits.length; i++) {
            const b = bits[i];
            const x1 = pLeft + i * bitWidth;
            const x2 = x1 + bitWidth;
            const xMid = x1 + bitWidth / 2;

            if (scheme === 'Unipolar NRZ') {
                const y = b === '1' ? baseY - 14 : baseY;
                if (i === 0) ctx.moveTo(x1, y);
                else ctx.lineTo(x1, y);
                ctx.lineTo(x2, y);
            } else if (scheme === 'Polar NRZ-L') {
                const y = b === '1' ? baseY - 14 : baseY + 14;
                if (i === 0) ctx.moveTo(x1, y);
                else ctx.lineTo(x1, y);
                ctx.lineTo(x2, y);
            } else if (scheme === 'Polar NRZ-I') {
                if (b === '1') lastLevel = -lastLevel;
                const y = lastLevel === 1 ? baseY - 14 : baseY + 14;
                if (i === 0) ctx.moveTo(x1, y);
                else ctx.lineTo(x1, y);
                ctx.lineTo(x2, y);
            } else if (scheme === 'Manchester') {
                // '1' is High-to-Low or Low-to-High depending on convention (IEEE 802.3: 0 is Low-to-High, 1 is High-to-Low)
                const yFirst = b === '1' ? baseY - 14 : baseY + 14;
                const ySecond = b === '1' ? baseY + 14 : baseY - 14;
                if (i === 0) ctx.moveTo(x1, yFirst);
                else ctx.lineTo(x1, yFirst);
                ctx.lineTo(xMid, yFirst);
                ctx.lineTo(xMid, ySecond);
                ctx.lineTo(x2, ySecond);
            } else if (scheme === 'Differential Manchester') {
                // Transition at beginning if 0, no transition if 1. Mid-bit always transitions.
                if (b === '0') lastLevel = -lastLevel;
                const y1 = lastLevel === 1 ? baseY - 14 : baseY + 14;
                const y2 = lastLevel === 1 ? baseY + 14 : baseY - 14;
                if (i === 0) ctx.moveTo(x1, y1);
                else ctx.lineTo(x1, y1);
                ctx.lineTo(xMid, y1);
                ctx.lineTo(xMid, y2);
                ctx.lineTo(x2, y2);
                lastLevel = -lastLevel;
            } else if (scheme === 'AMI') {
                let y = baseY;
                if (b === '1') {
                    y = amiSign === 1 ? baseY - 14 : baseY + 14;
                    amiSign = -amiSign;
                }
                if (i === 0) ctx.moveTo(x1, y);
                else ctx.lineTo(x1, y);
                ctx.lineTo(x2, y);
            }
        }
        ctx.stroke();
    });
}

// ==========================================
// 14. MODULE 4: NYQUIST & SHANNON CAPACITY
// ==========================================
function initCapacitySimulator() {
    const btn = document.getElementById('cap-calc-btn');
    if (!btn) return;
    btn.addEventListener('click', calculateChannelCapacity);
}

function calculateChannelCapacity() {
    const bw = parseFloat(document.getElementById('cap-bw').value); // in kHz
    const levels = parseInt(document.getElementById('cap-levels').value);
    const snrDb = parseFloat(document.getElementById('cap-snr').value);
    const resBox = document.getElementById('cap-result-box');

    const bwHz = bw * 1000;
    const nyquistBps = 2 * bwHz * Math.log2(levels);
    const snrLinear = Math.pow(10, snrDb / 10);
    const shannonBps = bwHz * Math.log2(1 + snrLinear);
    const maxLevels = Math.floor(Math.sqrt(1 + snrLinear));

    resBox.innerHTML = `
        <div class="card p-3 bg-surface border rounded-3 small font-mono mt-3">
            <h6 class="fw-bold text-primary mb-2"><i class="bi bi-reception-4"></i> Bandwidth &amp; Channel Capacity Analysis</h6>
            <div class="row g-2">
                <div class="col-md-6">
                    <div class="p-2 border rounded bg-light text-dark">
                        <strong>Nyquist Bit Rate (Noiseless Channel):</strong>
                        <div class="fs-5 text-primary fw-bold">${(nyquistBps / 1000).toFixed(2)} kbps</div>
                        <small class="text-muted">Formula: C = 2B &times; log2(L)</small>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="p-2 border rounded bg-light text-dark">
                        <strong>Shannon Capacity Limit (Noisy Channel):</strong>
                        <div class="fs-5 text-success fw-bold">${(shannonBps / 1000).toFixed(2)} kbps</div>
                        <small class="text-muted">Formula: C = B &times; log2(1 + SNR)</small>
                    </div>
                </div>
            </div>
            <div class="alert alert-info py-2 px-3 small mt-3 mb-0">
                <strong>Theoretical Limit:</strong> To avoid exceeding Shannon capacity on this channel, the maximum number of discrete signal levels must not exceed <strong>${maxLevels}</strong>.
            </div>
        </div>
    `;
}

// ==========================================
// 15. MODULE 4: SNMP MANAGER-AGENT MIB EXPLORER
// ==========================================
function initSnmpSimulator() {
    const btn = document.getElementById('snmp-send-btn');
    if (!btn) return;
    btn.addEventListener('click', runSnmpSimulation);
}

function runSnmpSimulation() {
    const oid = document.getElementById('snmp-oid').value;
    const pdu = document.getElementById('snmp-pdu').value;
    const outBox = document.getElementById('snmp-out-box');

    const mibData = {
        '1.3.6.1.2.1.1.1.0': { name: 'sysDescr.0', type: 'OCTET STRING', val: 'Linux VJCET-GW 5.15.0-generic x86_64' },
        '1.3.6.1.2.1.1.3.0': { name: 'sysUpTime.0', type: 'TimeTicks', val: '43289100 (5 days, 00:14:51.00)' },
        '1.3.6.1.2.1.1.4.0': { name: 'sysContact.0', type: 'OCTET STRING', val: 'Prof. Anju Markose <csd@vjcet.com>' },
        '1.3.6.1.2.1.2.1.0': { name: 'ifNumber.0', type: 'INTEGER', val: '4 Interfaces' },
        '1.3.6.1.2.1.4.1.0': { name: 'ipForwarding.0', type: 'INTEGER', val: '1 (Forwarding Enabled)' }
    };

    const target = mibData[oid] || { name: 'Custom OID', type: 'OCTET STRING', val: 'SNMP_VALUE_OK' };

    outBox.innerHTML = `
        <div class="card p-3 bg-dark text-light font-mono small rounded-3 mt-2">
            <div class="text-warning fw-bold mb-1"><i class="bi bi-arrow-left-right"></i> SNMP PDU Exchange Trace</div>
            <div class="text-info">&rarr; Manager Sent: ${pdu} [RequestID: 0x4A2B, OID: ${oid} (${target.name})]</div>
            <div class="text-success">&larr; Agent Reply: ResponsePDU [ErrorStatus: 0 (noError), ErrorIndex: 0]</div>
            <div class="mt-2 p-2 bg-black rounded text-light">
                <div><strong>Resolved OID:</strong> ${target.name} (${oid})</div>
                <div><strong>ASN.1 Data Type:</strong> ${target.type}</div>
                <div><strong>Variable Value:</strong> <span class="text-warning">${target.val}</span></div>
            </div>
        </div>
    `;
}

// ==========================================
// 16. LAB VIDEO PLAYERS & ANIMATED TERMINALS
// ==========================================
function initLabVideoPlayers() {
    const playBtns = document.querySelectorAll('.lab-run-terminal-btn');
    playBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const terminalBody = btn.closest('.lab-demo-card').querySelector('.animated-terminal-body');
            const lines = terminalBody.getAttribute('data-lines').split('|');
            terminalBody.innerHTML = '';
            btn.classList.add('disabled');

            let idx = 0;
            const timer = setInterval(() => {
                if (idx < lines.length) {
                    const lineDiv = document.createElement('div');
                    lineDiv.className = 'font-mono small my-1 animate-fade-in';
                    lineDiv.innerHTML = lines[idx];
                    terminalBody.appendChild(lineDiv);
                    terminalBody.scrollTop = terminalBody.scrollHeight;
                    idx++;
                } else {
                    clearInterval(timer);
                    btn.classList.remove('disabled');
                }
            }, 600);
        });
    });
}

function escapeHtml(text) {
    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
