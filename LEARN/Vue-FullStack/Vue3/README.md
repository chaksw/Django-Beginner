# 1. [VueJS 3.0](https://cn.vuejs.org/)

## 1.1. Chapter 1: Vue Base

### 1.1.1. Precondition

> Versions of Node.js > 15.0
> [How to update Node.js](https://juejin.cn/post/7161634586824212488)
> Install `vue`: `npm install -g @vue/cli`

### 1.1.2. Create Vue Project

`npm init vue@latest`
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

1. `Project name:` 项目名称，**不能存在大写**
2. `Add TypeScript?`: 是否添加`TypeScript`
3. `Add JSX Suppor?`: 是否添加`JSX`语法支持, `JSX`是`ReactJS`的特有文件后缀
4. `Add Vue Router for Single Page Application develipment?`: 是否添加 Vue 路由
5. `Add Pinia for state management?`: 是否添加`Pinia`状态管理
6. `Add Vitest for Unit Testing?` : 单元测试功能
7. `Add an End-to-End Testing Solution?` : 端对端测试
8. `Add ESLint for code quality? `: 代码质量相关

项目创建完成后会提示执行一下命令：

```bash
Done. Now run:

  cd vue-base
  npm install # 安装dependencies
  npm run dev # 运行项目
```

### 1.1.3. 安装`cnpm`

> `cnpm` 是 `npm`的国内淘宝镜像，会比`npm`要快
>
> 1. 安装命令：`sudo npm install -g cnpm --registry=https://registry.npm.taobao.org`
> 2. 查看版本：`cnpm -v`

### Vue Project Structure

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
