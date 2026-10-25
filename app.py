import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="景观减法｜扬州文旅交互研究",
    page_icon="🏮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---- Visual system ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&family=Noto+Sans+SC:wght@300;400;500;600&display=swap');
html, body, [class*="css"] { font-family: 'Noto Sans SC', sans-serif; }
.stApp { background: #f5f2eb; color: #272a25; }
section[data-testid="stSidebar"] { background: #202b27; }
section[data-testid="stSidebar"] * { color: #f4efe3 !important; }
.hero {
    padding: 3rem 3.2rem; border-radius: 18px;
    background: linear-gradient(115deg, rgba(24,42,36,.95), rgba(48,69,58,.84)),
                radial-gradient(circle at 80% 15%, #b49a68, transparent 35%);
    color: #f8f3e8; margin-bottom: 1.4rem;
}
.eyebrow { letter-spacing: .22em; text-transform: uppercase; font-size: .76rem; color: #d8c79f; }
.hero h1 { font-family: 'Noto Serif SC', serif; font-size: clamp(2.2rem, 4vw, 3.7rem); line-height: 1.22; margin: .8rem 0; }
.hero p { color: #e5e0d4; max-width: 760px; line-height: 1.9; font-size: 1rem; }
.section-title { font-family: 'Noto Serif SC', serif; font-size: 1.7rem; margin: .8rem 0 .35rem; color: #26352e; }
.section-sub { color: #6c7068; margin-bottom: 1rem; }
.panel { background: #fffdf8; border: 1px solid #e6dfd2; padding: 1.1rem 1.25rem; border-radius: 14px; }
.metric { background: #fffdf8; border: 1px solid #e6dfd2; padding: 1rem 1.2rem; border-radius: 12px; }
.metric-label { font-size: .82rem; color: #77786f; }
.metric-value { font-family: 'Noto Serif SC', serif; font-size: 1.8rem; color: #2b493d; margin-top: .2rem; }
.small-note { font-size: .82rem; color: #77786f; }
div[data-testid="stMetric"] { background: #fffdf8; padding: 1rem; border-radius: 12px; border: 1px solid #e6dfd2; }
.stButton button { border-radius: 8px; }
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
SAMPLE_CSV = DATA_DIR / "sample_survey.csv"

def load_sample():
    if SAMPLE_CSV.exists():
        return pd.read_csv(SAMPLE_CSV)
    return pd.DataFrame({
        "场景": ["瘦西湖夜景", "瘦西湖夜景", "瘦西湖夜景", "东关街店招", "东关街店招", "东关街业态"],
        "评价维度": ["灯光舒适度", "中式氛围", "光污染感知", "店招协调度", "文化辨识度", "业态多样性"],
        "满意度": [4.0, 4.3, 2.4, 3.1, 3.7, 2.8],
        "样本量": [86, 86, 86, 74, 74, 74],
    })

def heading(title, subtitle=""):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="section-sub">{subtitle}</div>', unsafe_allow_html=True)

def hero(title, subtitle, eyebrow="YANGZHOU · CULTURAL LANDSCAPE"):
    st.markdown(f"""
    <div class="hero">
      <div class="eyebrow">{eyebrow}</div>
      <h1>{title}</h1>
      <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🏮 景观减法")
    st.caption("扬州文旅交互研究 · 原型版")
    page = st.radio("探索模块", [
        "项目总览", "瘦西湖｜灯光优化", "东关街｜业态优化", "调查数据｜效果评估", "项目说明"
    ])
    st.markdown("---")
    st.caption("研究主线")
    st.markdown("**减去过度表达，留下文化本真。**")
    st.caption("注：当前内置为演示数据，不能作为正式调查结论。")

if page == "项目总览":
    hero("让景观回归恰到好处", "从瘦西湖夜景灯光与东关街商铺业态出发，探索“减法”如何改善文化景观体验。以游客感知为依据，让传统风貌、商业活力与游览舒适度取得平衡。")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric"><div class="metric-label">研究对象</div><div class="metric-value">两类场景</div><div class="small-note">园林夜景 × 历史街区</div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric"><div class="metric-label">研究视角</div><div class="metric-value">游客感知</div><div class="small-note">审美、舒适度与文化认同</div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric"><div class="metric-label">研究方法</div><div class="metric-value">调查 + 对比</div><div class="small-note">问卷、现场观察与方案评估</div></div>', unsafe_allow_html=True)
    heading("研究框架", "从问题识别到方案反馈，形成可验证的优化闭环。")
    steps = st.columns(4)
    for col, num, title, desc in zip(
        steps, ["01", "02", "03", "04"],
        ["发现问题", "理解感知", "提出减法", "评估效果"],
        ["灯光过强、视觉干扰；店招与业态趋同", "收集游客评价与偏好", "控制亮度、减少冗余、突出文化重点", "对比满意度与文化氛围评价"]
    ):
        with col:
            st.markdown(f'<div class="panel"><div class="eyebrow" style="color:#9b8352">{num}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
    st.markdown("")
    st.info("使用方式：从左侧选择场景，体验优化选项；在“调查数据”中上传你们自己的 CSV/Excel 数据。")

elif page == "瘦西湖｜灯光优化":
    hero("瘦西湖 · 夜景灯光减法", "目标不是简单地“变暗”或“变亮”，而是控制眩光与色彩杂乱，让桥、亭、树影和水面成为视觉主角。", "CASE 01 · SLENDER WEST LAKE")
    heading("交互式灯光方案", "调整下方参数，查看方案方向变化。当前为概念演示，不代表真实照明测算。")
    col1, col2 = st.columns([1, 1.2], gap="large")
    with col1:
        brightness = st.slider("整体亮度倾向", 1, 10, 6, help="1 = 更克制，10 = 更明亮")
        color_temp = st.select_slider("色温风格", options=["暖黄（约2700K）", "暖白（约3000K）", "中性白（约4000K）"], value="暖白（约3000K）")
        accent = st.selectbox("重点照明对象", ["桥与亭台", "古树与岸线", "水面倒影", "整体均匀照明"])
        clutter = st.slider("冗余装饰光 / 彩色光", 0, 10, 3, help="0 = 尽量减少，10 = 很多")
    with col2:
        # Conceptual preview generated with HTML/CSS, not a photorealistic rendering.
        warmth = {"暖黄（约2700K）": "#f1c879", "暖白（约3000K）": "#ffe5ae", "中性白（约4000K）": "#e5eee8"}[color_temp]
        glow = 0.12 + brightness * 0.035
        clutter_text = "保留少量必要引导光" if clutter <= 3 else ("需要进一步压缩彩色光源" if clutter <= 6 else "视觉干扰较强，建议显著减少")
        focus_text = {
            "桥与亭台": "以桥、亭台的轮廓光为主，避免全景平均照亮。",
            "古树与岸线": "用低位、遮光良好的灯具表达树形与岸线层次。",
            "水面倒影": "控制直射水面的光束，优先呈现自然倒影。",
            "整体均匀照明": "建议转为分区照明，避免每个对象获得同等亮度。"
        }[accent]
        st.markdown(f"""
        <div style="border-radius:16px; overflow:hidden; min-height:310px; position:relative;
          background:linear-gradient(180deg,#172c2c 0%,#25443d 48%,#101e1e 100%); padding:25px;
          box-shadow: inset 0 0 50px rgba(0,0,0,.25);">
          <div style="color:#e8dfc5;letter-spacing:.15em;font-size:.78rem">概念氛围预览 · 非实景渲染</div>
          <div style="height:120px;display:flex;align-items:end;justify-content:center;gap:12px;margin-top:8px">
            <div style="width:110px;height:78px;border:3px solid {warmth};border-bottom:0;border-radius:55% 55% 0 0;filter:drop-shadow(0 0 12px {warmth});opacity:{min(.95,glow+0.3)}"></div>
            <div style="width:70px;height:54px;border:2px solid {warmth};border-bottom:0;border-radius:55% 55% 0 0;opacity:{min(.9,glow+0.2)}"></div>
          </div>
          <div style="height:3px;background:{warmth};opacity:{min(.9,glow+.15)};box-shadow:0 0 18px {warmth};margin-top:0"></div>
          <div style="height:65px;background:linear-gradient(180deg,rgba(109,160,145,{glow}),rgba(20,38,37,.2));transform:perspective(80px) rotateX(8deg);filter:blur(1px)"></div>
          <div style="position:absolute;bottom:20px;left:25px;color:#f4ebd8;font-size:.9rem">{color_temp} · 亮度倾向 {brightness}/10</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("")
    a, b = st.columns(2)
    with a:
        st.markdown("#### 当前方案建议")
        st.write(focus_text)
        st.write(clutter_text)
    with b:
        st.markdown("#### 建议原则")
        st.write("• 控制眩光，避免灯具直射游客视线。")
        st.write("• 优先突出桥、亭、树与水面层次。")
        st.write("• 统一色温，减少无明确叙事作用的彩色光。")
    st.warning("正式方案应结合现场照度、灯具配光、生态影响与文物保护要求，由专业人员现场复核。")

elif page == "东关街｜业态优化":
    hero("东关街 · 商业表达减法", "通过减少重复、规范视觉秩序、保留在地文化内容，让历史街区不只是“看起来古”，而是更能讲述扬州的故事。", "CASE 02 · DONGGUAN STREET")
    heading("业态与店招方案配置", "选择你希望优先改善的方向，生成一份可讨论的初步建议。")
    priorities = st.multiselect("优先优化的内容", ["店招尺寸与色彩", "重复同质化商品", "传统手艺与地方文化展示", "步行空间与外摆秩序", "夜间照明与导视"], default=["店招尺寸与色彩", "重复同质化商品", "传统手艺与地方文化展示"])
    preservation = st.select_slider("传统风貌保留程度", options=["适度更新", "平衡协调", "优先保护"], value="平衡协调")
    commercial = st.select_slider("商业活力目标", options=["低干预", "稳步优化", "积极调整"], value="稳步优化")
    recommendations = {
        "店招尺寸与色彩": "建立店招尺度、材质与色彩指引，减少高亮灯箱和互相遮挡，允许有文化依据的个性表达。",
        "重复同质化商品": "先通过店铺业态普查识别重复品类，再以引导、孵化和租赁政策逐步增加差异化，不宜简单一刀切。",
        "传统手艺与地方文化展示": "为扬州漆器、玉雕、剪纸等在地文化内容创造可体验、可讲述的空间，避免只做符号化装饰。",
        "步行空间与外摆秩序": "划分连续步行通道与合理外摆区，优先保障通行、安全和无障碍体验。",
        "夜间照明与导视": "统一导视层级，控制过亮招牌和眩光，重点照亮街巷节点、历史建筑与必要的行走路径。"
    }
    st.markdown("#### 方案建议")
    if not priorities:
        st.info("请至少选择一项优化重点。")
    else:
        for i, item in enumerate(priorities, 1):
            st.markdown(f'<div class="panel" style="margin-bottom:.7rem"><strong>{i:02d} · {item}</strong><p style="margin:.5rem 0 0">{recommendations[item]}</p></div>', unsafe_allow_html=True)
    st.markdown("#### 当前策略定位")
    st.write(f"风貌策略：**{preservation}**；商业调整：**{commercial}**。")
    st.caption("以上为讨论用策略草案，具体实施需要店铺普查、商户访谈和管理规则共同支撑。")
    if st.button("导出本页优化建议为 CSV"):
        out = pd.DataFrame({"优化重点": priorities, "建议": [recommendations[x] for x in priorities]})
        st.download_button("下载建议文件", out.to_csv(index=False).encode("utf-8-sig"), "东关街优化建议.csv", "text/csv")

elif page == "调查数据｜效果评估":
    hero("用数据检验减法是否有效", "上传你们实际收集的问卷数据，查看不同场景、不同评价维度的结果。页面自带的示例数据仅用于演示图表功能。", "EVIDENCE · SURVEY INSIGHTS")
    uploaded = st.file_uploader("上传 CSV 或 Excel 文件", type=["csv", "xlsx"])
    if uploaded is not None:
        try:
            df = pd.read_csv(uploaded) if uploaded.name.lower().endswith(".csv") else pd.read_excel(uploaded)
            st.success(f"已读取文件：{uploaded.name}")
        except Exception as e:
            st.error(f"读取失败：{e}")
            df = load_sample()
    else:
        df = load_sample()
        st.info("当前显示演示数据。请上传真实问卷数据以替换。")
    st.markdown("#### 数据预览")
    st.dataframe(df, use_container_width=True, hide_index=True)
    numeric = df.select_dtypes(include="number").columns.tolist()
    cats = df.select_dtypes(exclude="number").columns.tolist()
    if len(df) > 0 and numeric:
        left, right = st.columns(2)
        with left:
            y_col = st.selectbox("选择数值指标", numeric, index=0)
            x_options = cats if cats else [y_col]
            x_col = st.selectbox("按哪个维度分组", x_options, index=0)
            if x_col != y_col:
                grouped = df.groupby(x_col, dropna=False)[y_col].mean().reset_index()
                fig = px.bar(grouped, x=x_col, y=y_col, title=f"{y_col}：分组均值", color=x_col)
                fig.update_layout(paper_bgcolor="#fffdf8", plot_bgcolor="#fffdf8", font_color="#30352f")
                st.plotly_chart(fig, use_container_width=True)
        with right:
            if len(numeric) >= 2:
                x_num = st.selectbox("相关性图 X 轴", numeric, index=0, key="xnum")
                y_num = st.selectbox("相关性图 Y 轴", numeric, index=min(1, len(numeric)-1), key="ynum")
                fig2 = px.scatter(df, x=x_num, y=y_num, color=cats[0] if cats else None, title="指标关系探索")
                fig2.update_layout(paper_bgcolor="#fffdf8", plot_bgcolor="#fffdf8", font_color="#30352f")
                st.plotly_chart(fig2, use_container_width=True)
            else:
                st.markdown('<div class="panel"><strong>分析提示</strong><p>如果想比较不同人群，请在问卷数据中保留年龄段、到访频率、场景等分类字段。</p></div>', unsafe_allow_html=True)
    st.caption("注意：不同问卷题目的量表方向、缺失值和样本量应先核对；相关关系不能直接解释为因果关系。")

else:
    hero("项目说明与下一步", "这是一个可运行的第一版交互原型。它展示了网站结构、交互逻辑与数据可视化的基本流程。", "ABOUT THIS PROTOTYPE")
    heading("目前已实现")
    for item in [
        "四个主要内容模块与侧边导航",
        "瘦西湖灯光参数交互与概念预览",
        "东关街优化重点选择与建议生成",
        "CSV / Excel 数据上传、预览与图表分析",
        "适配桌面浏览器的基础视觉样式",
    ]:
        st.markdown(f"- {item}")
    heading("建议的下一阶段")
    st.markdown("""
    1. 用你们自己拍摄的瘦西湖、东关街照片替换概念预览。
    2. 统一问卷字段，例如场景、题目、评分、年龄段、到访频率。
    3. 增加真实的前后对比滑块、图像热点和改造方案说明。
    4. 把调查结论与具体改进措施逐条对应，形成“证据—方案—反馈”链条。
    5. 部署为公开网页，供比赛答辩现场扫码体验。
    """)
    st.warning("当前版本不含账号系统、在线问卷提交后端或数据库；上传的数据仅在当前会话中用于分析。")

st.markdown("---")
st.markdown('<div style="text-align:center;color:#858579;font-size:.8rem;padding:.5rem">景观减法 · 扬州文旅交互研究原型 | 演示用途，数据结论以实际调查为准</div>', unsafe_allow_html=True)
