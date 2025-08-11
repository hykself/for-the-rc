import streamlit as st
import pandas as pd
import plotly.express as px

# 设置页面配置
st.set_page_config(
    page_title="西安交大Robocon历年成绩展示",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1a5276;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2980b9;
        margin-top: 1.5rem;
    }
    .achievement-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stat-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .stat-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #e74c3c;
    }
    .stat-label {
        font-size: 1rem;
        color: #7f8c8d;
    }
</style>
""", unsafe_allow_html=True)

# 页面标题
st.markdown('<h1 class="main-header">西安交通大学Robocon机器人队历年成绩展示</h1>', unsafe_allow_html=True)

# 团队简介
with st.container():
    st.markdown('<h2 class="sub-header">团队简介</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://i.imgur.com/placeholder.png", caption="西安交大Robocon机器人队", use_column_width=True)
    with col2:
        st.markdown("""
        西安交通大学机器人俱乐部(ABU ROBOCON机器人队)成立于2001年10月，连续参赛23年。
        队员秉承"优秀是我们的习惯，拼搏是我们的传统"队训，刻苦努力、不断奋进。
        
        作为国内首支获得国际冠军的队伍，西安交大Robocon机器人队在历届大赛中屡创佳绩，
        培养了大批优秀的工程技术人才，为国家科技创新事业做出了积极贡献。
        
        近日，第二十四届全国大学生机器人大赛总决赛中，西安交大ROBOCON机器人队在机器人篮球赛、
        仿生足式挑战赛和机器人排球赛三大赛项中荣获全国一等奖6项（其中排球赛项全国冠军，
        "飞身上篮"技能挑战赛全国季军，竞技赛全国八强），二等奖和三等奖共6项。
        """)

# 关键统计数据
with st.container():
    st.markdown('<h2 class="sub-header">历史成就概览</h2>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="stat-card"><div class="stat-value">4</div><div class="stat-label">国内冠军</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><div class="stat-value">2</div><div class="stat-label">国际冠军</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><div class="stat-value">8</div><div class="stat-label">国内季军</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-card"><div class="stat-value">4</div><div class="stat-label">最佳设计奖</div></div>', unsafe_allow_html=True)

# 历年成绩数据
robocon_data = {
    "年份": ["2025", "2024", "2020", "历史总计"],
    "赛事名称": [
        "第二十四届全国大学生机器人大赛ROBOCON",
        "第二十三届全国大学生机器人大赛ROBOCON",
        "第十九届全国大学生机器人大赛ROBOCON",
        "累计获奖情况"
    ],
    "主要奖项": [
        "全国一等奖6项（排球赛项全国冠军，\"飞身上篮\"技能挑战赛全国季军，竞技赛全国八强）、二等奖和三等奖共6项",
        "全国一等奖4项（排球赛项全国季军）、二等奖3项、三等奖1项",
        "全国一等奖、最佳设计奖（全国唯一）",
        "国内冠军4次、国际冠军2次、国内季军8次、最佳设计奖4次"
    ],
    "参赛项目": [
        "机器人篮球赛、仿生足式挑战赛、机器人排球赛（主题：飞身上篮）",
        "颗粒归仓、仿生和排球机器人竞赛",
        "绿茵争锋（机器人橄榄球比赛）",
        "多项赛项累计"
    ]
}

df = pd.DataFrame(robocon_data)

# 历年成绩表格
with st.container():
    st.markdown('<h2 class="sub-header">历年比赛成绩</h2>', unsafe_allow_html=True)
    st.dataframe(
        df,
        column_config={
            "年份": st.column_config.TextColumn(
                "年份",
                width="small"
            ),
            "赛事名称": st.column_config.TextColumn(
                "赛事名称",
                width="medium"
            ),
            "主要奖项": st.column_config.TextColumn(
                "主要奖项",
                width="large"
            ),
            "参赛项目": st.column_config.TextColumn(
                "参赛项目",
                width="large"
            )
        },
        hide_index=True,
        use_container_width=True
    )

# 奖项分布可视化
with st.container():
    st.markdown('<h2 class="sub-header">奖项分布</h2>', unsafe_allow_html=True)
    
    # 模拟奖项分布数据
    award_data = {
        "奖项类型": ["全国一等奖", "全国二等奖", "全国三等奖", "最佳设计奖", "国际冠军", "国际季军"],
        "数量": [13, 3, 1, 4, 2, 1]
    }
    award_df = pd.DataFrame(award_data)
    
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(
            award_df,
            values="数量",
            names="奖项类型",
            title="奖项分布比例",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(
            award_df,
            x="奖项类型",
            y="数量",
            title="奖项数量统计",
            color="奖项类型",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_layout(xaxis_title=None, yaxis_title="获奖数量")
        st.plotly_chart(fig, use_container_width=True)

# 历年参赛项目
with st.container():
    st.markdown('<h2 class="sub-header">历年参赛项目</h2>', unsafe_allow_html=True)
    
    project_data = {
        "年份": [2025, 2024, 2020],
        "项目数量": [3, 3, 1],
        "项目名称": [
            "篮球、仿生足式、排球",
            "颗粒归仓、仿生、排球",
            "绿茵争锋（橄榄球）"
        ]
    }
    project_df = pd.DataFrame(project_data)
    
    fig = px.bar(
        project_df,
        x="年份",
        y="项目数量",
        hover_data=["项目名称"],
        title="历年参赛项目数量",
        color="项目数量",
        color_continuous_scale=px.colors.sequential.Reds
    )
    fig.update_layout(xaxis_title="年份", yaxis_title="参赛项目数量")
    st.plotly_chart(fig, use_container_width=True)

# 团队风采
with st.container():
    st.markdown('<h2 class="sub-header">团队风采</h2>', unsafe_allow_html=True)
    
    # 团队照片展示
    st.write('### 比赛精彩瞬间')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('pic/1D0A31CB8968AFC08C759C31ECEA31E4.jpg', caption='第二十四届全国大学生机器人大赛现场', use_container_width=True)
    with col2:
        st.image('pic/AD438B7D4857E9FF9760BC26CEE63A51.jpg', caption='团队获奖合影', use_container_width=True)
    with col3:
        st.image('pic/C3475D83146B9CB8C95870C4DCD0829C.jpg', caption='机器人队年度合影', use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('pic/C859F7675B5FEBABF51107EB7B450BCF.jpg', caption='比赛精彩瞬间', use_container_width=True)
    with col2:
        st.image('pic/DD38753C585A9F32164882EA14E40FE3.jpg', caption='团队协作', use_container_width=True)
    with col3:
        st.image('pic/16095DA2A5E91DB079D70477A90F6A94.jpg', caption='机器人设计细节', use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('pic/7C3D27E670B41801CE502B9A38F472DD.jpg', caption='比赛准备阶段', use_container_width=True)
    with col2:
        st.image('pic/82E9ACDA75C7591173BE329A023F35E8.jpg', caption='技术调试', use_container_width=True)
    with col3:
        st.image('pic/8C9490C25A90D43176FB8570D9AB94E8.jpg', caption='颁奖仪式', use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image('pic/C04BD63841DC720F16477FFB8DEE8F01.jpg', caption='团队讨论', use_container_width=True)
    with col2:
        st.image('pic/F0BA66A312EB4EB8CDF8BF3F7636B6CB.jpg', caption='实验室日常', use_container_width=True)

    # 队内分工介绍
    st.write('### 队内分工')
    division_data = {
        '部门': ['机械组', '电控组', '视觉组', '协调组'],
        '主要职责': [
            '负责机器人结构设计、建模与制造',
            '负责电路设计、嵌入式开发与控制系统搭建',
            '负责图像处理、目标识别与算法优化',
            '负责项目管理、宣传推广与团队建设'
        ],
        '所需技能': [
            'CAD/ SolidWorks, 机械原理, 材料力学',
            'C/C++, 单片机开发, 自动控制原理',
            'Python/OpenCV, 机器学习, 深度学习',
            '沟通协调, 活动策划, 文档撰写'
        ]
    }

    df_division = pd.DataFrame(division_data)
    st.dataframe(df_division, use_container_width=True)

    # 招新信息
with st.container():
    st.write('### 加入我们')

# 自定义卡片样式
st.markdown('''
<style>
.card {
    background-color: #f5f5f5;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}
.card-header {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 10px;
    color: #2c3e50;
}
.requirement {
    background-color: #e8f4fd;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
}
.learning {
    background-color: #e6f7e9;
    padding: 10px;
    border-radius: 5px;
}
</style>
''', unsafe_allow_html=True)

# 招新卡片布局
cols = st.columns(2)

# 机械组卡片
with cols[0]:
    st.markdown('''
<div class="card">
    <div class="card-header">机械组</div>
    <div class="requirement">
    <strong>需要基础:</strong>
    <ul>
        <li>机械原理基础知识</li>
        <li>具备CAD/SolidWorks建模能力者优先</li>
        <li>了解基本加工工艺</li>
    </ul>
    </div>
    <div class="learning">
    <strong>可以学到:</strong>
    <ul>
        <li>机械结构设计与优化</li>
        <li>三维建模与仿真</li>
        <li>材料选型与力学分析</li>
        <li>精密加工与装配调试</li>
    </ul>
    </div>
</div>
''', unsafe_allow_html=True)

# 电控组卡片
with cols[1]:
    st.markdown('''
<div class="card">
    <div class="card-header">电控组</div>
    <div class="requirement">
    <strong>需要基础:</strong>
    <ul>
        <li>C/C++编程基础</li>
        <li>电路原理基础知识</li>
        <li>了解单片机者优先</li>
    </ul>
    </div>
    <div class="learning">
    <strong>可以学到:</strong>
    <ul>
        <li>嵌入式系统开发</li>
        <li>自动控制算法实现</li>
        <li>传感器数据处理</li>
        <li>PCB设计与制作</li>
    </ul>
    </div>
</div>
''', unsafe_allow_html=True)

# 视觉组卡片
with cols[0]:
    st.markdown('''
<div class="card">
    <div class="card-header">视觉组</div>
    <div class="requirement">
    <strong>需要基础:</strong>
    <ul>
        <li>Python编程基础</li>
        <li>了解OpenCV者优先</li>
        <li>具备基本数学基础</li>
    </ul>
    </div>
    <div class="learning">
    <strong>可以学到:</strong>
    <ul>
        <li>图像处理与目标识别</li>
        <li>机器学习算法应用</li>
        <li>机器人视觉定位</li>
        <li>实时数据处理</li>
    </ul>
    </div>
</div>
''', unsafe_allow_html=True)

# 协调组卡片
with cols[1]:
    st.markdown('''
<div class="card">
    <div class="card-header">协调组</div>
    <div class="requirement">
    <strong>需要基础:</strong>
    <ul>
        <li>良好沟通能力</li>
        <li>活动策划经验</li>
        <li>基本文档撰写能力</li>
    </ul>
    </div>
    <div class="learning">
    <strong>可以学到:</strong>
    <ul>
        <li>项目管理技能</li>
        <li>团队协作与领导力</li>
        <li>宣传推广与新媒体运营</li>
        <li>技术文档与报告撰写</li>
    </ul>
    </div>
</div>
''', unsafe_allow_html=True)

# 通用招新信息
st.markdown('### 招募要求')
col1, col2 = st.columns(2)
with col1:
    st.markdown('''
- **招募对象**: 西安交通大学全体本科生
- **基本要求**: 热爱机器人技术，有团队合作精神
- **时间要求**: 能保证每周固定时间参与研发
''')
with col2:
    st.markdown('''
- **选拔流程**: 报名 → 笔试 → 面试 → 培训考核
- **报名方式**: 关注机器人队官方通知
- **截止日期**: 每年秋季学期第4周
''')

st.success('零基础同学也可申请，我们提供系统培训！优秀者可获得保研加分、竞赛获奖证书及企业实习机会。')

st.info('注: 以上信息参考国内高校Robocon团队通用架构,具体以西安交大Robocon机器人队实际设置为准。官方照片将在获取后更新。')

# 数据来源说明
with st.container():
    st.markdown("""
    <div style="margin-top: 2rem; padding: 1rem; background-color: #f0f2f6; border-radius: 5px;">
        <h4 style="color: #555;">数据来源说明</h4>
        <p style="color: #666; font-size: 0.9rem;">
        本页面数据来源于西安交通大学新闻网及公开报道，最新更新时间: 2025年7月。
        部分年份数据可能不完整，如有更新信息，欢迎联系补充。
        </p>
    </div>
    """, unsafe_allow_html=True)

# 页脚
st.markdown("""
<div style="text-align: center; margin-top: 3rem; color: #888;">
    <p>© 2025 西安交通大学Robocon机器人队成绩展示 | 数据可视化项目</p>
</div>
""", unsafe_allow_html=True)