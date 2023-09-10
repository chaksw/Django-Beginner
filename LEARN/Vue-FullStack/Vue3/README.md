# 1. [VueJS 3.0](https://cn.vuejs.org/)

# 2. Chapter 1: Vue Base

## 2.1. Precondition

> Versions of Node.js > 15.0
> [How to update Node.js](https://juejin.cn/post/7161634586824212488)
> Install `vue`: `npm install -g @vue/cli`

## 2.2. Create Vue Project

1. `npm init vue@latest`
   这一指令将会安装并执行`create-vue`，它是 Vue 官方的项目脚手架工具。执行后将会看到一些诸如 TypeScript 和测试支持之类的可选功能提示

```bash
✔ Project name: … vue-base
✔ Add TypeScript? … No / Yes
✔ Add JSX Support? … No / Yes
✔ Add Vue Router for Single Page Application development? … No / Yes
✔ Add Pinia for state management? … No / Yes
✔ Add Vitest for Unit Testing? … No / Yes
✔ Add an End-to-End Testing Solution? › No
✔ Add ESLint for code quality? … No / Yes
```

> 1. `Project name:` 项目名称，**不能存在大写**
> 2. `Add TypeScript?`: 是否添加`TypeScript`
> 3. `Add JSX Suppor?`: 是否添加`JSX`语法支持, `JSX`是`ReactJS`的特有文件后缀
> 4. `Add Vue Router for Single Page Application develipment?`: 是否添加 Vue 路由
> 5. `Add Pinia for state management?`: 是否添加`Pinia`状态管理
> 6. `Add Vitest for Unit Testing?` : 单元测试功能
> 7. `Add an End-to-End Testing Solution?` : 端对端测试
> 8. `Add ESLint for code quality? `: 代码质量相关

2. 项目创建完成后会提示执行一下命令：

```bash
Done. Now run:

  cd vue-base
  npm install # 安装dependencies
  npm run dev # 运行项目
```

## 2.3. 安装`cnpm`

> `cnpm` 是 `npm`的国内淘宝镜像，会比`npm`要快
>
> 1. 安装命令：`sudo npm install -g cnpm --registry=https://registry.npm.taobao.org`
> 2. 查看版本：`cnpm -v`

# 3. Vue Project Structure

![project-structure](image.png)

```js
.vscode         --- VSCODE工具的配置文件
node_modules    --- Vue项目的运行依赖文件夹,执行npm install时，依赖文件会安装到这里
public          --- 资源文件夹（浏览器图标）
src             --- 源码文件夹
.gitignore      --- git忽略文件
index.html      --- 入口HTMl文件
package.json    --- 信息描述文件
README.md       --- 项目描述文件
vite.config.js  --- Vue配置文件
```

# `Template` Syntax - 模版语法

> Vue 使用一种基于`HTML`的模版语法，使我们能够声明式地将其组件实例的数据绑定到呈现的 DOM 上，所有的`Vue`模版都是语法层面合法的`HTML`，可以被符合规范的浏览器和`HTML`解析器解析

## Text Interpolation - 文本插值

最基本的数据绑定形式时文本差值（Text Interpolation， 它使用的是 "Mustache" 语法（即双大括号 `{{ }}`）：

```html
<template>
    <p>{{ msg }}</p>
</template>

<script>
    export default {
        data() {
            return {
                msg: "神奇的魔法",
            };
        },
    };
</script>
```

## Using JavaScript Expressions

每一个绑定仅支持单一表达式，也就是一段能够被求值的`JavaScript`代码。一个简单的判断代码是是否可以合法写在`return`后面。

```html
<template>
    <p>{{ number + 1 }}</p>
    <p>{{ ok ? 'Yes' : 'No' }}</p>
    <p>{{ mssage.split('').reverse().join('') }}</p>
</template>

<script>
    export default {
        data() {
            return {
                number: 10,
                ok: true,
                message: "大家好",
            };
        },
    };
</script>
```

## 原始`HTML`

双大括号将会将数据插值为纯文本，而不是`HTML`。若想插入`HTML`，则需要使用`v-html`指令

```html
<template>
    <p>纯文本: {{ rawHtml }}</p>
    <p>
        属性：
        <span v-html="rawHtml"></span>
    </p>
</template>
<script>
    export default {
        data() {
            return {
                rawHtml: "<a href='https://www.google.com'>Google</a>",
            };
        },
    };
</script>
```

# Attribute Bindings - 属性绑定

文本差值`{{}}`不能用在`HTML` attributes 中。想要响应式地绑定一个 attribute,应该使用`v-bind`指令

```html
<template>
    <div v-bind:id="dynamicId" v-bind:class="dynamicClass">Test</div>
</template>

<script>
    export default {
        data() {
            return {
                dynamicClass: "appClass",
                dynamicId: "appID",
            };
        },
    };
</script>

<style>
    .appClass {
        color: red;
        font-size: 30px;
    }
</style>
```

`v-bind`指令指示 Vue 将元素的`id`attribute 与组件的`dynamicId`属性保持一致。如果绑定的值是`null`或者`undefined`，那么该 attribute 将会从渲染的元素上移除

### Shorthand - 简写

因为`v-bind`非常常用，我们提供了特定的简写语法

```html
<div :id="dynamicId" :class="dynamicClass"></div>
```

## Boolean Attributes - 布尔型 Attribute

布尔型 attribute 依据 true/false 值来决定 attribute 是否应该存在于该元素上，`disabled`就是最常见的例子之一

```html
<button :disabled="isButtonDisabled">Button</button>
```

## Dynamically Binding Multiple Attributes - 动态绑定多个值

如果你有像这个一个包含多个 attribute 的 JavaScript 对象

```js
const objectOfAttrs = {
    id: "container",
    class: "wrappper",
};
```

# Conditional Rendering - 条件渲染

-   `v-if`
-   `v-else`
-   `v-else-if`
-   `v-show`

## `v-if`

`v-if` 指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回真值时才被渲染

## `v-else`

也可以使用`v-else`为`v-if`添加一个“else 区块“

> 一个元素`v-else`必须跟在一个`v-if`或者`v-else-if`元素后面，否则它将不会被识别。

## `v-else-if`

顾名思义，`v-else-if` 提供的是相应于`v-if`的"else if 区块“。它可以连续多次重复使用

> 和`v-else`类似，一个使用`v-else-if`的元素必须紧跟在一个`v-if`或一个`v-else-if`元素后面

## `v-show`

另一个可以用来按条件显示一个元素的指令是`v-show`。其用法基本一样：

不用之处在于`v-show`会在 DOM 渲染中保留该元素；`v-show`仅切换了该元素上名为`display`的 CSS 属性。

`v-show` 不支持在`<template>`元素上使用，也不能和`v-else`搭配使用。

## `v-if` VS `v-show`

`v-if` 是"真实的"按条件渲染，因为它确保了在切换时，条件区块内的条件监听器和子组件都会被销毁与重建。
`v-if` 也是**惰性**的：如果在初次渲染时条件值为 false，则不会做任何事。条件区块只有当条件首次变为 true 时才被渲染。‘
相比之下，`v-show`简单许多，元素无论初始条件如何，始终会被渲染，只有 CSS`display`属性会被切换。
总的来说，`v-if`有更高的切换开销，而`v-show`有更高的初始渲染开销。因此，如果需要频繁切换，则使用`v-show`较好；如果运行时绑定条件很少改变，则`v-if`会更为合适。

```html
<template>
    <h3>Conditional Rendering</h3>
    <div v-if="flag">Can u see me ?</div>
    <div v-else>Then u should see me</div>
    <div v-if="type === 'A'">A</div>
    <div v-else-if="type === 'B'">B</div>
    <div v-else-if="type === 'C'">C</div>
    <div v-else>Not A/B/C</div>
    <div v-show="flag">Can u see me ?</div>
</template>

<script>
    export default {
        data() {
            return {
                flag: true,
                type: "B",
            };
        },
    };
</script>
```

# List Rendering - 列表渲染

我们可以使用`v-for`指令基于一个数组来渲染一个列表。`v-for`指令的值需要使用`item in items`形式的特殊语法，其中`items`是源数据的数组，`item`是迭代项的别名.
在`v-for`快中可以完整地访问父作用域内的数据和变量。`v-for`也支持可选的第二个参数表示当前项的位置索引。

```html
<template>
    <h3>List Rendering</h3>
    <p v-for="name in names">{{ name }}</p>
</template>

<script>
    export default {
        data() {
            return {
                names: ["Chris", "Lyrics", "Murphy"],
            };
        },
    };
</script>
```

## 复杂数据

大多数情况，我们渲染的数据源来源于网络请求，也就是`JSON`格式

```html
<template>
    <h3>List Rendering</h3>
    <div v-for="item in results">
        <p>{{ item.title }}</p>
        <!-- 属性绑定 -->
        <img :src="item.avator" alt="" />
    </div>
</template>

<script>
    export default {
        data() {
            return {
                results: [
                    {
                        id: 2261677,
                        title: "鄂尔多斯｜感受一座城市的璀璨夜景 感受一座城市，除了白日里的车水马龙，喧嚣繁华之",
                        avator: "https://pic.qyer.com/avatar/002/25/77/30/200?v=1560226451",
                    },
                    {
                        id: 2261566,
                        title: "成都这家洞穴暗黑风咖啡厅酷毙了！！早C晚A走起☕️ 成都天气这么🔥 咖啡🌟人必备",
                        avator: "https://pic.qyer.com/avatar/002/25/77/30/200?v=1560226451",
                    },
                    {
                        id: 2261662,
                        title: "[川西新龙-措卡湖]措卡湖吗，意为“乱世从中的黑色海水”，神秘小众 原汁原味。",
                        avator: "https://pic.qyer.com/avatar/002/25/77/30/200?v=1560226451",
                    },
                ],
            };
        },
    };
</script>
```

`v-for`也支持使用可选的第二个参数表示当前项的位置索引

```html
<template>
    <h3>List Rendering</h3>
    <p v-for="(item, index) in names">{{ item }} - {{ index }}</p>
</template>

<script>
    export default {
        data() {
            return {
                names: ["Chris", "Lyrics", "Murphy"],
            };
        },
    };
</script>
```

也可以使用`of`作为分隔符来替代`in`,这更接近 JavaScript 的迭代器语法

```html
<div v-for="item of items"></div>
```

## `v-for`对象

也可以使用`v-for`来遍历一个对象的所有属性

```html
<template>
    <h3>List Rendering</h3>
    <!-- 默认遍历顺序 -->
    <div v-for="(value, key, index) in userInfo">
        <p>{{ index }}- {{ key }}-{{ value }}</p>
    </div>
    <!-- <p>{{ userInfo.name }}-{{ userInfo.age }}-{{ userInfo.sex }}</p> -->
</template>

<script>
    export default {
        data() {
            return {
                userInfo: {
                    // key : value
                    name: "iwen",
                    age: 20,
                    sex: "male",
                },
            };
        },
    };
</script>
```
