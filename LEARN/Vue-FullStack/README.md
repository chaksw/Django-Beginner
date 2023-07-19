# [VueJS](https://vuejs.org/)-based full stack CRM Project

## Start

### Installation and Creation

```bash
npm install @vue/cli
```

Check vue version after installation

```bash
vue --version
```

Create project (name： ganarcrm_vue)

```bash
vue create ganarcrm_vue
```

### Dependencies & Libraries

1. bulma (css framework)
   In project folder

```bash
npm install bulma
```

2. bulma-toast (as said a library to make it easy to show notifications to the users )

```bash
npm install bulma-toast
```

3. Axios (Talk to backend)

```bash
npm install axios
```

## Project setup & execution

To execution project

```bash
npm run serve
```

1. In main.js of `vue` project, setting baseURL using `axios`

```js
...
import axios from "axios"; // import axios

// setting a default URL to response
// after this setting, only relative path is required in the following everytime we send request using axios
axios.defaults.baseURL = "http://127.0.0.1:8000";

createApp(App).use(store).use(router, axios).mount("#app");
```

2. In App.vue, import `bulma` css framework，then all the frontend components of porject can use `bulma`

```vue
...
<style lang="scss">
@import "../node_modules/bulma";
</style>
```

3. In folder `components` (components is the location where we build reuseable front-end template) create `layout` folder and a `Navbar.vue` template file

```vue
<template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Ganr CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link class="button is-success" to="/sign-up">
                            <strong>Sign Up</strong>
                        </router-link>
                        <router-link class="button is-success" to="/log-in">
                            Log in
                        </router-link>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>
<!-- export as name "Navbar" -->
<script>
export default {
    name: "Navbar",
};
</script>
```

## Project structure

### VueJs based front-end

From a design architecture perspective, each folder in the created project can be considered that has it's role, building togetoher the component tree of frontend.

1. `router/index.js`: where we render the relation between component and custom URL, the `routes` defined reflect `<router-view></router-view>` in `App.vue`
2. `App.vue` :
    1. Root component, play role of top-level component in the component tree, where we build the overall structure and layout of applicaiton
    2. Routing Container: the only place that can contains the `<router-view>`
    3. Global Styles and Resources, all the styles and resoures inclued(`@import`) in `App.vue` can be shared and used throughtout the applicaiton.
    4. Global State Mangement...
3. `views/*vue`: where we create sub-page of project.
4. `components/` where we create component for page in `views/*.vue` or `App.vue`, specially we can create `components/layout` folder to put all the overall layout
5. `store/index.js` where we can configure the view access door.

    1. 状态管理：store/index.js 是 Vuex Store 的入口文件，用于创建和配置 Vuex Store 对象。Vuex 是一个状态管理库，它将应用程序的共享状态集中管理，包括**数据**、**状态**和**业务逻辑**。

    2. 全局状态存储：在 store/index.js 中定义的 `state` 对象存储了应用程序的全局状态。**这些状态可以被应用程序中的任何组件访问和修改。**通过定义和管理这些全局状态，可以实现组件之间的数据共享和响应式更新。

    3. 状态变更的管理：store/index.js 定义了 `mutations`，用于管理和修改状态。通过 `mutations`，你可以声明一系列的状态变更操作，每个操作都有一个名称和相应的处理函数。这样，在组件中通过提交 `mutations`，可以安全地修改状态，同时保持状态变更的跟踪和记录。

    4. 异步操作和副作用管理：store/index.js 中的 `actions` 允许执行**异步操作**，例如发送网络请求、处理副作用等。`Actions` 提供了一种机制来触发 `mutations`，以响应异步操作的结果或处理其他副作用。通过定义 `actions`，你可以将异步操作和副作用的逻辑集中管理。

    5. 模块化和命名空间：store/index.js 支持将 Vuex Store 分割成多个模块，每个模块拥有自己的状态、mutations、actions 等。这样可以提高代码的可维护性和扩展性，并允许不同模块之间的协同工作。

### `this.$`

> `this.$` 是一个特殊的语法，用于访问 Vue 实例上的内置属性、方法和插件。
>
> 1. `this.$data`：访问 Vue 实例的数据对象。例如，`this.$data` 可以获取到 Vue 实例中定义的响应式数据。
> 2. `this.$props`：访问 Vue 实例的 prop 属性。如果组件具有 `prop` 属性，则可以使用 `this.$props` 获取传递给组件的 `prop` 数据。
> 3. `this.$emit()`：触发当前 Vue 实例上的自定义事件。通过调用 `this.$emit('eventName', payload)` 可以向父组件或其他监听该事件的组件发送事件。
> 4. `this.$refs`：访问 Vue 实例中被注册的子组件或 DOM 元素的引用。例如，可以使用 this.$refs.myComponent 来访问名为 "myComponent" 的子组件或 DOM 元素。
> 5. `this.$router`：访问 Vue Router 实例，用于在组件中进行路由导航。例如，`this.$router.push('/path')` 可以用于在组件中进行编程式路由跳转。
> 6. `this.$store`：访问 Vuex Store 实例，用于在组件中进行状态管理。通过 `this.$store.state` 可以访问 Vuex Store 中的状态数据。
>
> -   需要注意的是，this.$ 语法只能在 Vue 组件的上下文中使用。在其他非组件的上下文中，这个语法是无效的。
> -   通过使用 this.$ 语法，你可以方便地访问 Vue 实例上的内置属性和方法，以及访问 Vue 的插件（如 Vue Router 和 Vuex）。这提供了一种方便的方式来进行状态管理、路由导航和与组件交互。

### Django

#### Dependencies

1. pipenv
2. django rest framework
3. django-cors-headers
4. djoser (to simplify authentication and verification of users)

```bash
pipenv shell
pip install django djangorestframework django-cors-headers djoser
```
