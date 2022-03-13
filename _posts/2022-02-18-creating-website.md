---
title: '创建个人主页'
date: 2022-02-18
permalink: /posts/2022/02/creating-website/
toc: true
tags:
  - 中文
  - 个人网站
  - Website
  - GitHub
  - GitHub Pages
---

近日较为清闲，花点时间把个人主页稍微整理一下。
在此记录一下网站的创建与管理等过程，顺带练习一下写作...

{% include user_def %}

> 参考：[[1](https://lijian.ac.cn/posts/2018/11/homepage/), [2](https://jayrobwilliams.com/posts/2020/06/academic-website/), [3](https://jayrobwilliams.com/posts/2020/07/customizing-website/), [4](https://jayrobwilliams.com/posts/2020/08/website-content/)]

## 1. 动机

相较于 LinkedIn 等网站，个人主页有着更高的自由度，可以更好地展示自己各个方面的特点、分享自己的经历。
此外，我们还可以根据自己的喜好来设置和调整网页风格，或者通过个人主页来分享文章、图片与 PDF 文档等内容。

个人主页还能够让我们摆脱平台的束缚。
假设我们只通过知乎、简书、 CSDN 或者百度贴吧发表文章，那么一旦平台倒闭或者发生故障，或者文章由于平台的监管机制与不断变化的网络舆论环境而被删除，找回从前发表的文章就会变得困难重重。
而个人主页一般依托于个人服务器或者类似于 GitHub Pages (微软) 等网络服务提供商。
即使网络服务供应商停止提供服务，由于个人主页基本上本地编写，它的底稿并不会受到影响。
本地化的特性也使得个人主页更容易修改与更新。

更重要的是，有的时候个人主页对于一个 Ph.D. 学生或者学者教授来说是硬性要求。
既然如此，把它弄得漂亮一点也是理所应当了:)

## 2. 创建与托管主页

传统的个人主页都编写与运行在个人服务器上。
这就会造成服务器与域名租用等花销。
而且个人服务器还需要亲自维护，这对于非网络从业人员（比如说本人）来说并不是一件手到擒来的任务。

所幸，GitHub Pages 使得个人主页的创建与托管变得十分容易。
大致来说，用户只需要创建一个 `<GitHub username>.github.io` 的公共仓库，选择一个适合自己的 `Jekyll` 模板来制作网页并 `push` 到 GitHub 网站即可。
GitHub 会在云端自动编译项目。
编译完成后，我们就可以通过网址 `https://<GitHub username>.github.io` 来访问自己的主页了。

我的个人主页是基于 `academicpages` （[GitHub](https://github.com/academicpages/academicpages.github.io), [模板网站](https://academicpages.github.io/)）修改而来。
该模板较为美观与现代化，契合当代的大众审美，而且功能尚可，使用起来比较方便。
[官方网站](https://academicpages.github.io/)，[这篇中文博客](https://lijian.ac.cn/posts/2018/11/homepage/)与[这篇英文博客](https://jayrobwilliams.com/posts/2020/06/academic-website/)提供了关于创建、初始化与基础修改模板的详细信息，这里不再赘述。

然而，该模板的最后一次提交在2019年6月，距今已有一段时间。
而且该模板并不完善，其中存在着很多小 bug 与不足。
下面的内容是关于我个人使用该模板是遇到的问题和一些解决方法，在此列出以便自己与他人查阅。

## 3. 模板改造

### 3.1. 关键文件/目录位置

> 参考：[[官方指导](https://academicpages.github.io/markdown/), [Liquid syntax guide](https://shopify.github.io/liquid/tags/control-flow/)].  
> 下列文件/目录为 academicpages 模板中提供的文件/位置，与本网站略有出入。

* Basic config options: _config.yml
* Top navigation bar config: _data/navigation.yml
* Single pages: _pages/
* Collections of pages are .md or .html files in:
  * _publications/
  * _portfolio/
  * _posts/
  * _teaching/
  * _talks/
* Footer: _includes/footer.html
* Static files (like PDFs): /files/
* Profile image (can set in _config.yml): images/profile.png
- to edit side-bar personal information: `./_config.yml`
- to edit home page: `./_pages/about.md`
- to edit left side-bar elements: `./includes/author-profile`
- to edit the publications page: `./_pages/publications.md`
- icon location: `./assets/css/academicons.css`; for usage refer to `./includes/author-profile.html`.

### 3.2. 文章的撰写与编译

* Name a file ".md" to have it render in markdown, name it ".html" to render in HTML.
* Go to the [commit list](https://github.com/academicpages/academicpages.github.io/commits/master) (on your repo) to find the last version Github built with Jekyll. 
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built

### 3.3. 添加导航栏条目

1. 在 `./_config.yml` 文件 `collection` 与 `default` 条目下添加新的条目名称与属性（[参考](https://github.com/academicpages/academicpages.github.io/issues/50)）；
2. 在 `./data/_navigation.yml` 文件中创建新条目的导航栏索引;
3. 在 `./_pages/` 文件夹下创建新条目的索引页面（可以以 `./_pages/posts.html` 作为参考）；
4. （可选）创建以下划线开头新条目的文件夹并将相应博客的 markdown 文档保存其中。
   注意修改索引页面中对博客文档的引用路径（参考 `./_pages/posts.html` 与 `./_posts/` 中的文档）。

### 3.4. 自定义按钮样式

> 参考：[[3.4.1](https://jayrobwilliams.com/posts/2020/07/customizing-website/#pushing-buttons)].

模板在 `./_sass/_buttongs.scss` 文件中定义了按钮样式 `.btn` 。
我们可以直接使用 `markdown` 语法
```md
[<button name>](<buttong link>){: .btn}  // default button style
```
来创建按钮，效果类似于： [按钮](){: .btn} 。

除此之外， `./_sass/_buttongs.scss` 文件也提供了一些额外的按钮风格，比如 `small` ， `inverse` 或者 `warning`。
特定风格的按钮可以通过
```md
[<button name>](<buttong link>){: .btn--<style>}  // button with a specific style
```
来创建，例如： [反相按钮](){: .btn--inverse} 。

我们也可以通过 `sass` 语法来定义自己的按钮风格。
[这篇文章](https://jayrobwilliams.com/posts/2020/07/customizing-website)中提供了一个自定义风格的示例。
在 `./_sass/_buttongs.scss` 文件中，我们可以添加名为 "research" 的按钮风格
```scss
/* research page buttons */
&--research {
  display: inline-block;
  margin-bottom: 0.25em;
  padding: 0.125em 0.25em;
  color: $link-color;
  text-align: center;
  text-decoration: none !important;
  border: 1px solid;
  border-color: $link-color;
  border-radius: $border-radius;
  cursor: pointer;

  &:hover {
    color: #fff;
    background-color: $link-color !important;
  }
}
```
到 `.btn` 域中。
代码中每个变量的含义一目了然，这里便不再赘述。
最终按钮效果可以参考[这个网站](https://jayrobwilliams.com/research/measurement/)和[我的“论文”页面](https://yinghao-li.github.io/publications/)。
两个网站中的按钮颜色不同的原因是它们使用了不同的主题颜色（由 `$link-color` 定义在文件 `./_sass/_variable.scss` 中）。

{{ hint_warning }}
我在本地通过 `jekyll server` 命令预览按钮样式时发现除了默认以外的风格几乎全部不能正常显示。
原因是 `jekyll server` 命令在本地运行时，使用了 `sass` 的 `--cache-location` 选项。
（！！！真的吗？上面一句是 Copilot 自动补全的。我本来想说原因未知，因为我不是专业人员……
我也不知道它说的对不对，请大家自行甄别。）
无论如何，该修改可以在 GitHub Pages 正常编译与显示，因此无需担心。
{{ _hint }}

### 3.5. 自定义高亮文本样式

一些网站（[示例](https://docs.docker.com/desktop/windows/install/)）使用了一些美观的高亮文本块来展示诸如“提示”、“警告”等信息。
然而，academicpages 模板除了 markdown 语法自带的“引用”样式以外并未提供类似的功能。
要实现类似的段落高亮功能，我们需要自行创建相应的 CSS 样式。

**创建并导入样式文件**

Academicpages 模板的大部分 CSS 样式都定义在 `./_sass/` 文件夹下的文件中。
我们可以直接将自己定义的 CSS 样式添加到任意文件中。
然而，一个更好的选择是在 `./_sass/` 文件夹下创建自己的 `_<css name>.scss` 文件来专门保存自定义的 CSS 样式以避免与模板的默认样式混淆。

假设我们想将自定义的 CSS 样式保存在 `./_sass/_user.scss` 文件中，那么除了创建并编写该文件以外，我们还需要在 `./assets/css/main.scss` 文件中添加如下代码来导入自定义样式：
```scss
@import "/user";  # 导入自定义样式
```

**编写 CSS 样式**

实际上，段落高亮的代码编写较为简单。
我们只需要为 `<div>` 标签新定义一个 `class` 属性，并修改该属性的“背景”、“边框”和“间距”等变量的值即可实现段落高亮。
下面的代码展示了一个在本工程中使用的简单的例子：
```scss
div.hint__info{
  font-size: $type-size-syntax;  # 字体大小
  padding-left: 1em;  # 左边距
  padding-top: 0.3em;  # 上边距
  padding-bottom: 0.3em;  # 下边距
  margin-top: 0.3em;  # 上间距
  margin-bottom: 1.3em;  # 下间距
  border-left-style: solid;  # 边框样式
  border-left-color:#6bf;  # 边框颜色
  background-color:rgba(102,187,255,.1);  # 背景颜色

  p {
    margin-bottom: 0em;  # 去除段落的默认间距
  }
}
```

最后，我们可以直接通过在 `<div>` 标签中使用 `class` 属性来调用样式，例如：
```html
<div class="hint__info" markdown=1>
  这是一个提示信息。
</div>
```
例中设置属性 `markdown=1` 是为了使该段落可以兼容 markdown 语法（[参考](https://stackoverflow.com/questions/29368902/how-can-i-wrap-my-markdown-in-an-html-div)）。

{{ hint_warning }}
注意：该属性未受所有网站支持。
{{ _hint }}

**使用 liquid 语法简化样式调用**

然而，直接使用 html 语法的调用方式稍显复杂。
我们可以通过 liquid 语法来将其简化。
例如，我们可以在 `./_includes` 文件夹下创建一个 `user_def` 文件（`.html`后缀可以省略也可以保留），并在其中定义如下变量：
```liquid
\{\% assign hint_info = "<div class=hint__info markdown=1>" \%\} 
\{\% assign _hint = "</div>" \%\}
```

{{ hint_warning }}
注意：由于代码块中的 liquid 语法会被直接解析而无法显示，我在大括号 `{}` 和百分号 `%` 前添加了反斜线 `\` 以避免解析。
使用时请删除反斜线。
{{ _hint }}

为了可以使用该 liquid 语法，我们需要在目标 markdown 文件表头下方引用 `user_def` 文件：
```liquid
\{\% include user_def \%\}
```
最后，我们可以在该 markdown 文件中通过 liquid 语法来调用样式：
```liquid
\{\{ hint_info \}\}
  这是一个提示信息。
\{\{ _hint \}\}
```
最终效果类似于：

{{ hint_info }}
  这是一个提示信息。
{{ _hint }}

### 3.6. 设置 Google Analytics

> 参考：[[Issue 265](https://github.com/academicpages/academicpages.github.io/issues/265)]

如果要分析我们的个人网站的访问情况，Google Analytics 是一个非常有用的工具。
除了访问次数以外，它还能够显示当前活跃用户数目、用户访问时间与访问者地区等信息。

如果要将 Google Analytics 集成到我们的个人网站，我们首先需要创建 Universal Analytics 媒体资源。
具体操作步骤可以参考 [Universal Analytics 官方帮助文档](https://support.google.com/analytics/answer/10269537)。
**注意**：仅创建 Universal Analytics 媒体资源即可。

成功创建媒体资源后，我们可以看到格式为 `UA-XXXXX-X` 的 Tracking ID。
我们需要将该 Tracking ID 复制到 `_config.yml` 文件中的 `analytics/google/tracking_id` 条目下（需要在 ID 前后添加双引号），并将 `analytics/provider` 条目的值设置为 `custom`。
另外，我们还需要将 Google Analytics 管理页面中 js 格式的 Tracking Code 复制到 `_includes/analytics-providers/custom.html` 文件中。
Tracking Code 的具体位置为 `<Your Google Analytics Admin Webpage>/Admin/ADMIN/property/Tracking Info/Tracking Code/Global Site Tag (gtag.js)`，类似于：
```js
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=XXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'XXX');
</script>
```

保存改动到 Github Pages 后，我们就可以在 Google Analytics 页面查看我们个人网站的访问信息了。


## 后记

写中文文章竟然比英文文章更费劲？？？
使用 vim 写中文不断切输入法太痛苦了 :rofl:。
