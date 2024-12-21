# 第一次交流
## Latex使用的相关内容
### Latex 模板:
- % 用来注释
- \ 用来转移字符或者表示一些命令
- & 用于表格或数学公式中的位置对齐符号
- $ 用作数学公式标记，框在“$$ $$”中间的内容会被翻译成数学公式
- ~ 保留强制空格
- “^ ^”中间的内容变成上标，“_ _”中间的内容变成下标
- “{ }”中间的内容会被作为一个整体对待
- “#” 在编写宏包时使用
---
### 正文：
#### 设定区域：
- \documentclass{...}和\usepackege{...}为设定区域，规定论文格式，导入相关依赖包等
- 一般不会对生成的PDF产生影响
- 设定区域会随着我们不断添加新的元素而丰富
#### 正文区域：
- \begin ... \end 命令中间的区域为正文
- PDF中所有的可见内容都在此添加
- 正文区域需先输入一篇论文的基本内容，设定论文题目、摘要、关键字等
#### 各级标题：
- chapter 章，一般只用于成书
- section 节
- subsection 小节
- subsubsection 小小节
#### 文档命令：
- “\\\” 用于换行 e.g："\newline、\linebreak、\\\\[offset]"
- \par 分段
- \newpage 分页命令
- \setlength{\parindent}{长度} 用于首行缩进
---
### 数学公式：
#### 特殊字符和短公式：
- $公式$ 
#### 单行公式带编号
- ```latex
  \begin{quation} \label{公式标签}
  ……
  \end{equation}
- \autoref{公式标签} 自动引用（需要用 \usepackage{hyperref} 导入依赖包）
#### 无编号公式
- \\\[公式\\\] 或者 $$公式$$
#### 多行公式
- \begin{split} ... \end{split} (需要用 \usepackage{amsmath} 导入依赖包，有的环境可能自带)
#### 分情况讨论
- 属于多行公式一种，使用 \begin{cases} ... \end{cases} （需要用 \usepackage{amsmath} 导入依赖包，有的环境可能自带）
- 需要用正文样式输出的地方\text{}
---
### 图片
#### 插入图片：
- 依赖包graphicx（有的环境可能自带）
- 常用模板：
  ```latex
  \begin{figure}[htbp]
      \centering
      \includegraphics[图片大小][图片路径]
      \caption{图片标题、说明}
      \label{图片标签}
  \end{figure}
- [图片大小] 图片大小用height和width规定，单位采用cm或者inch；如果只输入其中一个量，则将保持宽高比插入。
- [图片路径] 图片相对于tex文件的路径。
- 部分双栏显示的模板：图片如果需要跨栏显示，则把\begin{figure}...\end{figure}改成\begin{figure*}...\end{figure*}即可。
- 注：插入图片尽可能插入 **矢量图** ！e.g：EPS、PDF格式的图片
---
### 表格
- 使用[表格生成器](https://www.latex-tables.com/)来制作表格和生成响应的Latex代码。
---
### 文献引用
#### 文末参考文献引用模式：
```latex
\begin{thebibliography}{99} %99表示引用上限
\bibitem{label1} Anite G ,V.B V ,John P.Hybrid model with optimal features for non-invasive blood glucose monitoring from breath biomarkers[J].Biomedical Signal Processing and Control,2024,88(PC):
\bibitem{label2}Zhining C ,Jianzhou W ,Li Y ,et al.A hybrid electricity load prediction system based on weighted fuzzy time series and multi-objective differential evolution[J].Applied Soft Computing,2023,149(PB):
\bibitem{label3}\url{http://www.latexstudio.net/}
\bibitem{label4}\url{http://www.chinatex.org/}
\end{thebibliography}
```
#### 引用文献方式：
- ```latex
  \cite{label} 
  ```
  用来在文中引用文献
#### 使用.bib文件来引用大量文献
1. 新建.bib文件
2. 在.tex文件中开头和引用处修改一定代码
3. 进入谷歌学术搜索文献，点击“引用”，点击BibTex，即可获得响应的Latex代码，复制到.bib文件中
- .bib文件中的格式：
  ```bibtex
  @article{yu2019review,
  title={A review of recurrent neural networks: LSTM cells and network architectures},
  author={Yu, Yong and Si, Xiaosheng and Hu, Changhua and Zhang, Jianxun},
  journal={Neural computation},
  volume={31},
  number={7},
  pages={1235-1270},
  year={2019},
  publisher={MIT Press One Rogers Street, Cambridge, MA 02142-1209, USA journals-info~...}
  }
  ```
#### 上标引用
1. .tex文件开头去除相应注释
2. 将\cite改为\upcite即可