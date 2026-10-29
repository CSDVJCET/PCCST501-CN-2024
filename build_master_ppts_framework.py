"""
build_master_ppts_framework.py
Core presentation builder and rich visual templates for PCCST501 Computer Networks.
Prepared exclusively for:
Prof. Anju Markose | Assistant Professor, Department of Computer Science & Engineering
Viswajyothi College of Engineering and Technology (VJCET), Vazhakulam
KTU 2024 Scheme Curriculum
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

# --- Color Theme Palette ---
COLOR_PRIMARY = RGBColor(15, 30, 74)       # Deep Navy Blue #0F1E4A
COLOR_SECONDARY = RGBColor(14, 116, 144)   # Deep Teal / Cyan #0E7490
COLOR_ACCENT = RGBColor(217, 119, 6)       # Warm Amber / Gold #D97706
COLOR_BG_DARK = RGBColor(15, 23, 42)       # Slate 900 #0F172A
COLOR_BG_DARK_SURFACE = RGBColor(30, 41, 59) # Slate 800
COLOR_TEXT_LIGHT = RGBColor(248, 250, 252) # Slate 50
COLOR_TEXT_DARK = RGBColor(15, 23, 42)     # Slate 900
COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
COLOR_CARD_BG = RGBColor(248, 250, 252)    # Slate 50
COLOR_CARD_BORDER = RGBColor(203, 213, 225)# Slate 300
COLOR_CARD_ACCENT_BG = RGBColor(238, 242, 255) # Indigo 50
COLOR_CARD_GREEN_BG = RGBColor(236, 253, 245)  # Emerald 50
COLOR_CARD_AMBER_BG = RGBColor(254, 243, 199)  # Amber 100

AUTHOR_TAG = "Prof. Anju Markose | Assistant Professor, Dept. of CSE | VJCET"
COURSE_TAG = "PCCST501 Computer Networks | KTU 2024 Scheme"
INSTITUTION_TAG = "Viswajyothi College of Engineering and Technology (VJCET), Vazhakulam"
WATERMARK_TEXT = "Prof. Anju Markose • VJCET CSE • PCCST501"

def init_prs():
    """Initializes a 16:9 widescreen presentation deck."""
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    return prs

def add_slide_decorations(slide, show_watermark=True):
    """Adds subtle footer and watermark to ensure brand integrity."""
    # Footer
    footer = slide.shapes.add_textbox(Inches(0.8), Inches(6.92), Inches(11.8), Inches(0.35))
    tf_f = footer.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = f"{COURSE_TAG} | {AUTHOR_TAG}"
    p_f.font.size = Pt(9.5)
    p_f.font.color.rgb = COLOR_TEXT_MUTED

    # Top right subtle watermark tag
    if show_watermark:
        wm = slide.shapes.add_textbox(Inches(7.5), Inches(6.92), Inches(5.0), Inches(0.35))
        tf_wm = wm.text_frame
        p_wm = tf_wm.paragraphs[0]
        p_wm.text = "Dept. of CSE, VJCET"
        p_wm.alignment = PP_ALIGN.RIGHT
        p_wm.font.size = Pt(9.5)
        p_wm.font.color.rgb = COLOR_TEXT_MUTED

def create_title_slide(prs, topic_code, title, subtitle, module_name):
    """Creates a modern, dark-themed title slide with gold ribbon and faculty watermark."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Dark Slate Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG_DARK
    bg.line.fill.background()
    
    # Top Subtle Banner Bar
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.15))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = COLOR_ACCENT
    top_bar.line.fill.background()
    
    # Left Vertical Gold Accent Ribbon
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(1.2), Inches(0.18), Inches(5.1))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_ACCENT
    bar.line.fill.background()
    
    # Main Text Box
    tx_box = slide.shapes.add_textbox(Inches(1.35), Inches(1.1), Inches(11.2), Inches(5.3))
    tf = tx_box.text_frame
    tf.word_wrap = True
    
    # Course & Module Header Tag
    p0 = tf.paragraphs[0]
    p0.text = f"{COURSE_TAG} • {module_name.upper()} • {topic_code}"
    p0.font.bold = True
    p0.font.size = Pt(13)
    p0.font.color.rgb = COLOR_ACCENT
    p0.space_after = Pt(10)
    
    # Main Title
    p1 = tf.add_paragraph()
    p1.text = title
    p1.font.bold = True
    p1.font.size = Pt(30)
    p1.font.color.rgb = COLOR_TEXT_LIGHT
    p1.space_after = Pt(12)
    
    # Subtitle / Scope
    p2 = tf.add_paragraph()
    p2.text = subtitle
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(148, 163, 184)
    p2.space_after = Pt(24)
    
    # Faculty Attribution Card
    p3 = tf.add_paragraph()
    p3.text = f"Prepared by: {AUTHOR_TAG}"
    p3.font.bold = True
    p3.font.size = Pt(13.5)
    p3.font.color.rgb = RGBColor(226, 232, 240)
    p3.space_after = Pt(3)

    p4 = tf.add_paragraph()
    p4.text = f"{INSTITUTION_TAG} • KTU S5 CSE"
    p4.font.size = Pt(11.5)
    p4.font.color.rgb = RGBColor(148, 163, 184)
    
    # Subtle Watermark Badge on Title Slide
    wm_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.2), Inches(5.6), Inches(3.3), Inches(0.9))
    wm_card.fill.solid()
    wm_card.fill.fore_color.rgb = COLOR_BG_DARK_SURFACE
    wm_card.line.color.rgb = COLOR_SECONDARY
    wm_card.line.width = Pt(1)
    
    wm_tx = slide.shapes.add_textbox(Inches(9.3), Inches(5.65), Inches(3.1), Inches(0.8))
    wm_tf = wm_tx.text_frame
    p_wm1 = wm_tf.paragraphs[0]
    p_wm1.text = "KTU B.Tech Curriculum"
    p_wm1.font.bold = True
    p_wm1.font.size = Pt(10.5)
    p_wm1.font.color.rgb = COLOR_ACCENT
    
    p_wm2 = wm_tf.add_paragraph()
    p_wm2.text = "Official Classroom Slide Deck"
    p_wm2.font.size = Pt(9.5)
    p_wm2.font.color.rgb = COLOR_TEXT_LIGHT
    
    return slide

def create_content_slide(prs, title, topic_tag, points, card_header=None, card_content=None):
    """Creates a structured lecture slide with top banner, deep content bullets, and optional takeaway card."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Top Navy Banner
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY
    banner.line.fill.background()
    
    # Gold Accent Line Under Banner
    banner_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.06), Inches(13.333), Inches(0.04))
    banner_line.fill.solid()
    banner_line.fill.fore_color.rgb = COLOR_ACCENT
    banner_line.line.fill.background()
    
    # Title
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.18), Inches(9.2), Inches(0.75))
    tf_t = tx_title.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.bold = True
    p_t.font.size = Pt(22)
    p_t.font.color.rgb = COLOR_TEXT_LIGHT
    
    # Topic Tag (Top Right)
    tx_tag = slide.shapes.add_textbox(Inches(9.0), Inches(0.18), Inches(3.6), Inches(0.75))
    tf_tag = tx_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = topic_tag
    p_tag.alignment = PP_ALIGN.RIGHT
    p_tag.font.bold = True
    p_tag.font.size = Pt(13)
    p_tag.font.color.rgb = COLOR_ACCENT
    
    # Left Content Box
    left_w = Inches(7.5) if card_header else Inches(11.8)
    tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), left_w, Inches(5.4))
    tf = tx_box.text_frame
    tf.word_wrap = True
    
    for i, pt in enumerate(points):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if isinstance(pt, tuple): # (Header, Description)
            p.text = f"• {pt[0]}"
            p.font.bold = True
            p.font.size = Pt(14.5)
            p.font.color.rgb = COLOR_PRIMARY
            p.space_after = Pt(2)
            
            p_sub = tf.add_paragraph()
            p_sub.text = f"   {pt[1]}"
            p_sub.font.size = Pt(12.5)
            p_sub.font.color.rgb = COLOR_TEXT_DARK
            p_sub.space_after = Pt(7)
        else:
            p.text = f"• {pt}"
            p.font.size = Pt(13.5)
            p.font.color.rgb = COLOR_TEXT_DARK
            p.space_after = Pt(7)
            
    # Right Highlight Card
    if card_header and card_content:
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), Inches(1.35), Inches(3.9), Inches(5.35))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_SECONDARY
        card.line.width = Pt(1.5)
        
        tx_card = slide.shapes.add_textbox(Inches(8.9), Inches(1.5), Inches(3.5), Inches(5.0))
        tf_c = tx_card.text_frame
        tf_c.word_wrap = True
        
        p_ch = tf_c.paragraphs[0]
        p_ch.text = card_header
        p_ch.font.bold = True
        p_ch.font.size = Pt(15)
        p_ch.font.color.rgb = COLOR_SECONDARY
        p_ch.space_after = Pt(10)
        
        for c_pt in card_content:
            p_c = tf_c.add_paragraph()
            p_c.text = f"→ {c_pt}"
            p_c.font.size = Pt(12)
            p_c.font.color.rgb = COLOR_TEXT_DARK
            p_c.space_after = Pt(6)
            
    add_slide_decorations(slide)
    return slide

def create_comparison_slide(prs, title, topic_tag, col1_title, col1_items, col2_title, col2_items, col3_title=None, col3_items=None):
    """Creates a structured comparison slide with 2 or 3 distinct vertical cards."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Top Banner
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY
    banner.line.fill.background()
    
    banner_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.06), Inches(13.333), Inches(0.04))
    banner_line.fill.solid()
    banner_line.fill.fore_color.rgb = COLOR_ACCENT
    banner_line.line.fill.background()
    
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.18), Inches(9.2), Inches(0.75))
    tf_t = tx_title.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.bold = True
    p_t.font.size = Pt(22)
    p_t.font.color.rgb = COLOR_TEXT_LIGHT
    
    tx_tag = slide.shapes.add_textbox(Inches(9.0), Inches(0.18), Inches(3.6), Inches(0.75))
    tf_tag = tx_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = topic_tag
    p_tag.alignment = PP_ALIGN.RIGHT
    p_tag.font.bold = True
    p_tag.font.size = Pt(13)
    p_tag.font.color.rgb = COLOR_ACCENT
    
    if col3_title:
        card_w = Inches(3.7)
        card_gap = Inches(0.3)
        cols = [(col1_title, col1_items, COLOR_PRIMARY), (col2_title, col2_items, COLOR_SECONDARY), (col3_title, col3_items, COLOR_ACCENT)]
    else:
        card_w = Inches(5.7)
        card_gap = Inches(0.4)
        cols = [(col1_title, col1_items, COLOR_PRIMARY), (col2_title, col2_items, COLOR_SECONDARY)]
        
    start_x = Inches(0.8)
    for idx, col_info in enumerate(cols):
        c_title, c_items, col_accent = col_info[0], col_info[1], col_info[2]
        cx = start_x + idx * (card_w + card_gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.35), card_w, Inches(5.35))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG if idx % 2 == 0 else COLOR_CARD_ACCENT_BG
        card.line.color.rgb = col_accent
        card.line.width = Pt(1.5)
        
        tx = slide.shapes.add_textbox(cx + Inches(0.2), Inches(1.5), card_w - Inches(0.4), Inches(5.0))
        tf = tx.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = c_title
        p0.font.bold = True
        p0.font.size = Pt(15.5)
        p0.font.color.rgb = col_accent
        p0.space_after = Pt(10)
        
        for item in c_items:
            p = tf.add_paragraph()
            if isinstance(item, tuple):
                p.text = f"• {item[0]}: {item[1]}"
            else:
                p.text = f"• {item}"
            p.font.size = Pt(12)
            p.font.color.rgb = COLOR_TEXT_DARK
            p.space_after = Pt(5)
            
    add_slide_decorations(slide)
    return slide

def create_numerical_slide(prs, title, topic_tag, problem_statement, formula_box, step_calculations, final_answer, exam_tip=None):
    """Creates a dedicated worked numerical problem slide."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Top Banner
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY
    banner.line.fill.background()
    
    banner_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.06), Inches(13.333), Inches(0.04))
    banner_line.fill.solid()
    banner_line.fill.fore_color.rgb = COLOR_ACCENT
    banner_line.line.fill.background()
    
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.18), Inches(9.2), Inches(0.75))
    tf_t = tx_title.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.bold = True
    p_t.font.size = Pt(22)
    p_t.font.color.rgb = COLOR_TEXT_LIGHT
    
    tx_tag = slide.shapes.add_textbox(Inches(9.0), Inches(0.18), Inches(3.6), Inches(0.75))
    tf_tag = tx_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = topic_tag
    p_tag.alignment = PP_ALIGN.RIGHT
    p_tag.font.bold = True
    p_tag.font.size = Pt(13)
    p_tag.font.color.rgb = COLOR_ACCENT
    
    # Left: Problem Statement & Formula Container
    p_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.35), Inches(6.0), Inches(5.35))
    p_card.fill.solid()
    p_card.fill.fore_color.rgb = COLOR_CARD_BG
    p_card.line.color.rgb = COLOR_PRIMARY
    p_card.line.width = Pt(1.5)
    
    tx_p = slide.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.6), Inches(5.0))
    tf_p = tx_p.text_frame
    tf_p.word_wrap = True
    
    p0 = tf_p.paragraphs[0]
    p0.text = "📌 KTU Numerical Problem Statement"
    p0.font.bold = True
    p0.font.size = Pt(14.5)
    p0.font.color.rgb = COLOR_PRIMARY
    p0.space_after = Pt(8)
    
    p1 = tf_p.add_paragraph()
    p1.text = problem_statement
    p1.font.size = Pt(12.5)
    p1.font.color.rgb = COLOR_TEXT_DARK
    p1.space_after = Pt(14)
    
    p2 = tf_p.add_paragraph()
    p2.text = "📐 Governing Formulas & Principles:"
    p2.font.bold = True
    p2.font.size = Pt(13.5)
    p2.font.color.rgb = COLOR_SECONDARY
    p2.space_after = Pt(6)
    
    for f in formula_box:
        pf = tf_p.add_paragraph()
        pf.text = f"• {f}"
        pf.font.size = Pt(12)
        pf.font.color.rgb = COLOR_TEXT_DARK
        pf.space_after = Pt(4)
        
    # Right: Step-by-Step Solution & Final Answer
    s_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(1.35), Inches(5.5), Inches(5.35))
    s_card.fill.solid()
    s_card.fill.fore_color.rgb = COLOR_CARD_GREEN_BG
    s_card.line.color.rgb = RGBColor(16, 185, 129)
    s_card.line.width = Pt(1.5)
    
    tx_s = slide.shapes.add_textbox(Inches(7.3), Inches(1.5), Inches(5.1), Inches(5.0))
    tf_s = tx_s.text_frame
    tf_s.word_wrap = True
    
    p_s0 = tf_s.paragraphs[0]
    p_s0.text = "📝 Step-by-Step Derivation & Solution"
    p_s0.font.bold = True
    p_s0.font.size = Pt(14.5)
    p_s0.font.color.rgb = RGBColor(4, 120, 87)
    p_s0.space_after = Pt(8)
    
    for step in step_calculations:
        p_st = tf_s.add_paragraph()
        p_st.text = f"Step {step[0]}: {step[1]}" if isinstance(step, tuple) else f"• {step}"
        p_st.font.size = Pt(12)
        p_st.font.color.rgb = COLOR_TEXT_DARK
        p_st.space_after = Pt(5)
        
    p_ans = tf_s.add_paragraph()
    p_ans.text = f"✅ FINAL ANSWER: {final_answer}"
    p_ans.font.bold = True
    p_ans.font.size = Pt(13)
    p_ans.font.color.rgb = RGBColor(4, 120, 87)
    p_ans.space_after = Pt(8)
    
    if exam_tip:
        p_tip = tf_s.add_paragraph()
        p_tip.text = f"💡 Exam Tip: {exam_tip}"
        p_tip.font.size = Pt(11)
        p_tip.font.color.rgb = COLOR_TEXT_MUTED
        
    add_slide_decorations(slide)
    return slide

def create_code_slide(prs, title, topic_tag, code_snippet, explanations, practical_significance=None):
    """Creates a slide for C / Linux Socket hands-on code and system calls."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Top Banner
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY
    banner.line.fill.background()
    
    banner_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.06), Inches(13.333), Inches(0.04))
    banner_line.fill.solid()
    banner_line.fill.fore_color.rgb = COLOR_ACCENT
    banner_line.line.fill.background()
    
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.18), Inches(9.2), Inches(0.75))
    tf_t = tx_title.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = title
    p_t.font.bold = True
    p_t.font.size = Pt(22)
    p_t.font.color.rgb = COLOR_TEXT_LIGHT
    
    tx_tag = slide.shapes.add_textbox(Inches(9.0), Inches(0.18), Inches(3.6), Inches(0.75))
    tf_tag = tx_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = topic_tag
    p_tag.alignment = PP_ALIGN.RIGHT
    p_tag.font.bold = True
    p_tag.font.size = Pt(13)
    p_tag.font.color.rgb = COLOR_ACCENT
    
    # Left: Monospaced Code Card
    code_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.35), Inches(6.8), Inches(5.35))
    code_card.fill.solid()
    code_card.fill.fore_color.rgb = COLOR_BG_DARK
    code_card.line.color.rgb = COLOR_SECONDARY
    code_card.line.width = Pt(1.5)
    
    tx_code = slide.shapes.add_textbox(Inches(0.95), Inches(1.45), Inches(6.5), Inches(5.1))
    tf_c = tx_code.text_frame
    tf_c.word_wrap = True
    
    p_ct = tf_c.paragraphs[0]
    p_ct.text = "// Linux Socket & Protocol Implementation"
    p_ct.font.bold = True
    p_ct.font.size = Pt(11)
    p_ct.font.color.rgb = COLOR_ACCENT
    p_ct.space_after = Pt(6)
    
    p_cd = tf_c.add_paragraph()
    p_cd.text = code_snippet
    p_cd.font.name = 'Consolas'
    p_cd.font.size = Pt(10.5)
    p_cd.font.color.rgb = RGBColor(226, 232, 240)
    
    # Right: Detailed Explanations
    exp_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.8), Inches(1.35), Inches(4.8), Inches(5.35))
    exp_card.fill.solid()
    exp_card.fill.fore_color.rgb = COLOR_CARD_BG
    exp_card.line.color.rgb = COLOR_PRIMARY
    exp_card.line.width = Pt(1.5)
    
    tx_exp = slide.shapes.add_textbox(Inches(8.0), Inches(1.5), Inches(4.4), Inches(5.0))
    tf_e = tx_exp.text_frame
    tf_e.word_wrap = True
    
    p_e0 = tf_e.paragraphs[0]
    p_e0.text = "⚙️ System Call & Execution Workflow"
    p_e0.font.bold = True
    p_e0.font.size = Pt(14)
    p_e0.font.color.rgb = COLOR_PRIMARY
    p_e0.space_after = Pt(8)
    
    for exp in explanations:
        p_ex = tf_e.add_paragraph()
        if isinstance(exp, tuple):
            p_ex.text = f"• {exp[0]}: {exp[1]}"
        else:
            p_ex.text = f"• {exp}"
        p_ex.font.size = Pt(12)
        p_ex.font.color.rgb = COLOR_TEXT_DARK
        p_ex.space_after = Pt(6)
        
    if practical_significance:
        p_ps = tf_e.add_paragraph()
        p_ps.text = f"💡 Hands-on Insight: {practical_significance}"
        p_ps.font.bold = True
        p_ps.font.size = Pt(11.5)
        p_ps.font.color.rgb = COLOR_SECONDARY
        
    add_slide_decorations(slide)
    return slide

def create_exam_booster_slide(prs, topic_tag, title, bloom_level, university_questions, key_takeaways):
    """Creates a revision, exam booster, and Bloom's Taxonomy alignment slide."""
    slide_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(slide_layout)
    
    # Top Banner
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_PRIMARY
    banner.line.fill.background()
    
    banner_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, Inches(1.06), Inches(13.333), Inches(0.04))
    banner_line.fill.solid()
    banner_line.fill.fore_color.rgb = COLOR_ACCENT
    banner_line.line.fill.background()
    
    tx_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.18), Inches(9.2), Inches(0.75))
    tf_t = tx_title.text_frame
    p_t = tf_t.paragraphs[0]
    p_t.text = f"🎯 Exam Booster & Review: {title}"
    p_t.font.bold = True
    p_t.font.size = Pt(21)
    p_t.font.color.rgb = COLOR_TEXT_LIGHT
    
    tx_tag = slide.shapes.add_textbox(Inches(9.0), Inches(0.18), Inches(3.6), Inches(0.75))
    tf_tag = tx_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = topic_tag
    p_tag.alignment = PP_ALIGN.RIGHT
    p_tag.font.bold = True
    p_tag.font.size = Pt(13)
    p_tag.font.color.rgb = COLOR_ACCENT
    
    # Left Card: University Questions
    q_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.35), Inches(5.8), Inches(5.35))
    q_card.fill.solid()
    q_card.fill.fore_color.rgb = COLOR_CARD_AMBER_BG
    q_card.line.color.rgb = COLOR_ACCENT
    q_card.line.width = Pt(1.5)
    
    tx_q = slide.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.4), Inches(5.0))
    tf_q = tx_q.text_frame
    tf_q.word_wrap = True
    
    p_q0 = tf_q.paragraphs[0]
    p_q0.text = f"📚 KTU High-Yield Questions ({bloom_level})"
    p_q0.font.bold = True
    p_q0.font.size = Pt(14.5)
    p_q0.font.color.rgb = COLOR_ACCENT
    p_q0.space_after = Pt(10)
    
    for q in university_questions:
        pq = tf_q.add_paragraph()
        pq.text = f"Q: {q}"
        pq.font.size = Pt(12)
        pq.font.color.rgb = COLOR_TEXT_DARK
        pq.space_after = Pt(7)
        
    # Right Card: Key Takeaways
    t_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.9), Inches(1.35), Inches(5.7), Inches(5.35))
    t_card.fill.solid()
    t_card.fill.fore_color.rgb = COLOR_CARD_ACCENT_BG
    t_card.line.color.rgb = COLOR_SECONDARY
    t_card.line.width = Pt(1.5)
    
    tx_t = slide.shapes.add_textbox(Inches(7.1), Inches(1.5), Inches(5.3), Inches(5.0))
    tf_t2 = tx_t.text_frame
    tf_t2.word_wrap = True
    
    p_t0 = tf_t2.paragraphs[0]
    p_t0.text = "💡 Critical Conceptual Takeaways"
    p_t0.font.bold = True
    p_t0.font.size = Pt(14.5)
    p_t0.font.color.rgb = COLOR_SECONDARY
    p_t0.space_after = Pt(10)
    
    for t in key_takeaways:
        pt = tf_t2.add_paragraph()
        pt.text = f"✔ {t}"
        pt.font.size = Pt(12)
        pt.font.color.rgb = COLOR_TEXT_DARK
        pt.space_after = Pt(6)
        
    add_slide_decorations(slide)
    return slide
