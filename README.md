# 景观减法｜扬州文旅交互展示平台

这是一个使用 Python + Streamlit 制作的网页原型，适合在本地运行和继续开发。

## 功能
- 项目总览与研究框架
- 瘦西湖夜景灯光参数交互（概念预览，不是实景渲染）
- 东关街店招、业态优化策略选择
- 上传 CSV / Excel 问卷数据，查看表格与图表
- 演示数据与使用说明

## 运行方法

建议使用 Python 3.10 或更新版本。

### Windows
1. 解压项目文件夹。
2. 在文件夹空白处打开终端/命令提示符。
3. 创建虚拟环境（可选但推荐）：
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
5. 启动网页：
   ```bash
   streamlit run app.py
   ```
6. 浏览器一般会自动打开 `http://localhost:8501`。

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## 调查数据格式建议
可上传 CSV 或 Excel。推荐字段：
- 场景：瘦西湖夜景 / 东关街店招 / 东关街业态
- 评价维度：灯光舒适度、文化氛围等
- 满意度：数值评分
- 样本量：该指标的有效样本数

正式分析时，最好使用每位受访者一行的原始问卷数据，以支持分组和统计检验。内置样例是演示数据，不可当作真实调查结果。

## 下一步可扩展
- 实景照片前后对比滑块
- 真实问卷收集与数据库
- 用户反馈提交与后台管理
- 更精细的响应式视觉设计
- 部署到云端并生成可分享网址
