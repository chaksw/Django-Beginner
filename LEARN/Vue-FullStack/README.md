-   [1. VueJS-based full stack CRM Project](#1-vuejs-based-full-stack-crm-project)
    -   [1.1. Vue Installation and Creation](#11-vue-installation-and-creation)
        -   [1.1.1. Dependencies \& Libraries (local)](#111-dependencies--libraries-local)
        -   [1.1.2. Project setup \& execution](#112-project-setup--execution)
-   [2. Project structure](#2-project-structure)
    -   [2.1. VueJs based front-end](#21-vuejs-based-front-end)
        -   [2.1.1. `this.$`](#211-this)
        -   [2.1.2. Interaction](#212-interaction)
            -   [2.1.2.1. `@submit.prevent`](#2121-submitprevent)
            -   [2.1.2.2. `v-model`](#2122-v-model)
            -   [2.1.2.3. `v-if` `v-for` `v-bind`](#2123-v-if-v-for-v-bind)
    -   [2.2. Django](#22-django)
        -   [2.2.1. Dependencies (Pipenv usage)](#221-dependencies-pipenv-usage)
        -   [2.2.2. Djoser](#222-djoser)
        -   [2.2.3. Django Rest Framework Authentication (Token)](#223-django-rest-framework-authentication-token)
            -   [2.2.3.1. Configuration of Token Based Authentication](#2231-configuration-of-token-based-authentication)

# 1. [VueJS](https://vuejs.org/)-based full stack CRM Project

## 1.1. Vue Installation and Creation

```bash
npm install -g @vue/cli
```

Check vue version after installation

```bash
vue --version
```

Create project (name： ganarcrm_vue)

```bash
vue create ganarcrm_vue
```

### 1.1.1. Dependencies & Libraries (local)

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

### 1.1.2. Project setup & execution

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

```js
...
<style lang="scss">
@import "../node_modules/bulma";
</style>
```

3. In folder `components` (components is the location where we build reuseable front-end template) create `layout` folder and a `Navbar.vue` template file

```js
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

# 2. Project structure

## 2.1. VueJs based front-end

![Structure](image.png)

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

### 2.1.1. `this.$`

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

### 2.1.2. Interaction

#### 2.1.2.1. `@submit.prevent`

> `@submit.prevent` 是 `Vue.js` 模板中用于监听表单提交事件的指令。它结合了` @submit` 和 `.prevent` 两个指令的功能。
> ` @submit`：这是 `Vue.js` 中的事件监听指令之一，用于监听表单提交事件。当表单提交时，会触发绑定的方法。
> `.prevent`：这是 `Vue.js` 中的事件修饰符之一，用于阻止默认事件的发生。在表单提交的情况下，`.prevent` 可以阻止浏览器默认地提交表单，从而避免页面刷新。

`@submit.prevent` 所对应的 `method` 在对应 component 的`export defaut{methods:{}}` 中实现或部署，以实现`submit`的对应逻辑

```js
<script>
export default {
    name: "SignUp",
    methods: {
        submitForm() {
            alert("Submit Form");
        },
    },
};
</script>
```

#### 2.1.2.2. `v-model`

> `v-model` 是 `Vue.js` 中用于实现双向数据绑定的指令。它用于在模板中将表单元素和 Vue 实例的数据进行双向绑定，使得数据的变化可以自动同步到视图，以及用户输入的变化可以自动更新到数据。双向绑定指的是数据的改变能够影响视图，而视图的改变也能够反过来影响数据。这使得开发者不需要显式地监听输入事件和手动更新数据，简化了表单交互和数据处理的过程。

```js
<input v-model="dataProperty">
```

> 在上面的示例中，`v-model` 绑定在一个 `<input>` 元素上，它会将 `<input>` 元素的值与 Vue 实例中的 `dataProperty` 数据属性进行双向绑定。
> 在 `data()` 中定义

```js
export default {
    data() {
        return {
            dataProperty: "",
        };
    },
};
```

`data()` 是` Vue.js` 组件选项对象中的一个函数，用于定义组件的初始数据。它的作用是返回一个对象，其中包含了组件需要**响应式追踪的数据**。
具体来说，`data()` 函数中返回的对象中的属性会成为 Vue 组件的响应式数据。这意味着当这些数据发生变化时，相关的视图会自动更新。

> `而后，当用户在输入框中输入内容时，dataProperty` 数据会自动更新为输入的值。同样地，当 `dataProperty` 数据发生变化时，输入框中的值也会随之更新。

#### 2.1.2.3. `v-if` `v-for` `v-bind`

> 当使用 `Vue.js` 开发应用时，`v-if`、`v-for` 和 `v-bind` 是常用的 `Vue.js` 模板指令，用于实现动态的条件渲染、列表渲染和属性绑定。

1. `v-if`：
   `v-if` 是 `Vue.js` 中的条件渲染指令，用于根据表达式的真假条件来决定是否渲染元素或组件。当表达式为真时，元素或组件会被渲染；当表达式为假时，元素或组件会被移除或隐藏。`v-if` 的特点是在每次条件切换时，元素或组件的创建和销毁都会触发，适用于需要频繁切换的情况。
2. `v-for`：
   `v-for` 是 `Vue.js` 中的列表渲染指令，用于遍历数组或对象，并将其内容渲染多次。通过 `v-for`，你可以遍历数组中的每一项，或者遍历对象的属性，然后使用当前项的值来渲染相应的元素或组件。你可以使用特定的语法形式来指定当前项的别名和索引，以及提供 `key` 属性来帮助 `Vue.js` 更高效地更新列表。
3. `v-bind`：
   `v-bind` 是 `Vue.js` 中的属性绑定指令，用于动态地将 `Vue` 实例中的数据绑定到 `HTML` 元素的属性上。通过 `v-bind`，你可以将 `Vue` 实例中的数据动态地绑定到元素的属性上，例如将变量绑定到元素的 `class`, `style` 或其他属性上。你可以使用简化的 `:attr` 形式来代替 `v-bind:attr`，使得模板更加简洁易读。

## 2.2. Django

### 2.2.1. Dependencies ([Pipenv](https://pypi.org/project/pipenv/#usage) usage)

1. pipenv
2. django rest framework
3. django-cors-headers
4. djoser (to simplify authentication and verification of users)

5. Generate `Pipfile.lock`

```bash
pipenv lock
```

2. Install Dependencies (install after `Pipfile.lock` file is generated)

```bash
pipenv shell
pipenv install django djangorestframework django-cors-headers djoser # install packages and generate dependencies description file (Pipfile.lock)
```

3. Generate `requirements.txt`

```bash
pipenv requirements > requirements
```

4. Install dependencies `requirements.txt`

```bash
pipenv install -r path/to/requirements. txt
```

### 2.2.2. [Djoser](https://djoser.readthedocs.io/en/latest/)

> PS: djoser 是一个用于 Django 的插件，它简化了用户认证和授权的处理。它提供了一组 RESTful API，用于处理用户注册、登录、密码重置等功能。使用 djoser，你可以轻松地设置和管理用户身份验证。

### 2.2.3. Django Rest Framework Authentication (Token)

#### 2.2.3.1. Configuration of Token Based Authentication

1. Add `rest_framework.authtoken` to `INSTALLED_APPS`:

```py
INSTALLED_APPS = [
    'django.contrib.auth',
    (...),
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    (...),
]
```

2. Configure `urls.py.` Pay attention to `djoser.url.authtoken` module path:

```py
urlpatterns = [
    (...),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
```

3. Add `rest_framework.authentication.TokenAuthentication` to Django REST Framework authentication strategies tuple:

```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        (...)
    ),
}
```

4. Run migrations - this step will create tables for `auth` and `authtoken` apps:

```py
python ./manage.py migrate
```
