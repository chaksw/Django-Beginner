-   [1. React](#1-react)
    -   [1.1. ReactJS for Python Backend Devs](#11-reactjs-for-python-backend-devs)
        -   [1.1.1. Requirement:](#111-requirement)
        -   [1.1.2. Recommandation](#112-recommandation)
    -   [1.2. Creation](#12-creation)
        -   [1.2.1. Related commands](#121-related-commands)
    -   [1.3. React based FontEnd Structure](#13-react-based-fontend-structure)
        -   [1.3.1. React 如何通过`index.js` 和 `App.js` 渲染前端`html`](#131-react-如何通过indexjs-和-appjs-渲染前端html)
            -   [1.3.1.1. 总结](#1311-总结)
        -   [1.3.2. Props Attribute](#132-props-attribute)
        -   [1.3.3. Class-based component](#133-class-based-component)
        -   [1.3.4. React HOOKs(`useState`) (new feature in react since v16.8)](#134-react-hooksusestate-new-feature-in-react-since-v168)
    -   [1.4. Development based on `Django` (backend) and `React` （frontend)](#14-development-based-on-django-backend-and-react-frontend)
        -   [1.4.1. Virtual Env](#141-virtual-env)
        -   [1.4.2. Back-End](#142-back-end)
        -   [1.4.3. Front-End](#143-front-end)
        -   [1.4.4. Connecting Back-End(Django) to Front-End(React) using Axios](#144-connecting-back-enddjango-to-front-endreact-using-axios)
        -   [1.4.5. Setting for interaction between Django and React](#145-setting-for-interaction-between-django-and-react)
    -   [1.5. Practice - Task Manager](#15-practice---task-manager)
        -   [1.5.1. Project Structure](#151-project-structure)

# 1. [React](https://react.dev/)

React is a JavaScript libraryt for buildingg user interfaces, the majority call **React** as framework as they compare it with the other front-end frameworks in the market (`Angular` & `Vue.js` )

React allows us to create an individual front-end component(as `.js` function) and then collect them like pieces of lego.

## 1.1. ReactJS for Python Backend Devs

this README is a summary of tutorial about how to use `ReactJS` as front-end for python django(as back-end) development.

### 1.1.1. Requirement:

1. Node.js installed (need `npm` as node package management) PS: npm is equivalent of `pip` in python
2. [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) (exetension in google chrome)
3. [create-react-app](https://github.com/facebook/create-react-app) (command line program)
    - Use `npx` (a package runner tool that comes with `npm 5.2+` and higher)

### 1.1.2. Recommandation

Vscode exetension

1. Shortcut for React dev: [ES7+ React/Redux/React-Native snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets)

## 1.2. Creation

### 1.2.1. Related commands

1. Creat React App
   In using command(`npx`) below, it will be going to download the more crecnt `create-react-app` release, so that we can make sure we won't use a outdated version.

```bash
npx create-react-app frontend #name of application
```

2. Start developement server
   Start development server and open the browser and run on localhose and listen on port:3000

```bash
npm start
```

3. Deploy application
   **Bundles** the app into static files for production.

```bash
npm run **build**
```

4. Test

```bash
npm test
```

## 1.3. React based FontEnd Structure

The main working space is `src` folder, and inside this folder:

1. `index.js` is React's App entry point, all other related files in this proejct are imported.

```js
import React from "react"; // library
import ReactDOM from "react-dom/client"; // library
import "./index.css"; // local files
import App from "./App"; // loacl files
import reportWebVitals from "./reportWebVitals"; // loac files

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
```

2. `App.js` define the `<App/>` component which is unique in a react application, it uses `JSX` (javascript xml) (a syntax that allow us to write html and also to insert javascript logic)
   Inside of `return`, only one component is allowed, so if we need multiple component to be defined in one return, we need to use `<div></div>`

```js
import logo from "./logo.svg";
import "./App.css";

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer">
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default App;
```

### 1.3.1. React 如何通过`index.js` 和 `App.js` 渲染前端`html`

1. 在`App.js`中，我们通过定义一个函数（或者类）来创建一个前端模块（语法为`JSX`）,并通过`export default App` 将其导出。
2. 而在`index.js`中，我们将`App.js`进行导入，并通过`.render`函数渲染，而渲染的对象则使用`DOM`在`public/index.html`中寻找 component 的`id`定位。

代码对应：
In `public/index.html`

```html
<!-- define a component with id='root' -->
<div id="root">...</div>
```

In `index.js`

```js
import App from "./App"; // import the App() function
...
// fetch html component using DOM
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);
```

In `App.js`

```js
import logo from "./logo.svg";
import "./App.css";
// define a componet as function
function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer">
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default App; // export App
```

3. 每一个由`function`定义的 component 在会可以作为一个`JSX`元素被调用，如：

```js
// define a 'Hello' function-based component
import React from "react";

// function syntax [to create a component]
function Hello() {
    return <h1>Hello Bek!</h1>;
}
export default Hello;
```

```js
// 在App.js中通过<Hello />调用该component
import "./App.css";
import Hello from "./components/Hello";
// Stateless component [functional component]
function App() {
    return (
        <div>
            <Hello />
        </div>
    );
}
export default App;
```

一般来说，自定义的 function based component 都创建在 component 文件夹中。

#### 1.3.1.1. 总结

1. 以`index.js`作为入口（连接`JSX`定义的 components 和`html`）；
2. `App.js`作为主窗口 layout，其中放入自定义的各种`JSX` components
3. 在`./components/.js`中定义各种 component unit，导入到`App.js`中

### 1.3.2. Props Attribute

Props can be considered as input parameter of component function, it's a collection attribute of component that allow us to use it's attribute when using in `App.js`

Example：

```js
// define a 'Hello' function-based component
import React from "react";

// function syntax [to create a component]
function Hello(props) {
    // here we define 'props' as input parameter and using it's name attribute
    return <h1>Hello {props.name}</h1>;
}
export default Hello;
```

```js
// 在App.js中通过<Hello />调用该component
import "./App.css";
import Hello from "./components/Hello";
// Stateless component [functional component]
function App() {
    return (
        // here we define a name attribute, which will be a 'props' attribute in Hello function
        <div>
            <Hello name="Luke Cage!" />
        </div>
    );
}
export default App;
```

### 1.3.3. Class-based component

```js
// Class based component [ES6 class based]
class Hello extends React.Component {
    render() {
        return <h1>Hello {this.props.name}</h1>;
    }
}

export default Hello;
```

### 1.3.4. React HOOKs(`useState`) (new feature in react since v16.8)

React Hook is the best pratice (for now) to build a component

example:
`Counter.js`

```js
import React, { useState } from "react";

function Counter() {
    // Declare a new state variables [variable and state function]
    const [count, setCount] = useState(100);
    return (
        <div>
            <h2>{count}</h2>
            <br></br>
            <button onClick={() => setCount(count + 100)}>Click Plus</button>
            <br></br>
            <br></br>
            <button onClick={() => setCount(count - 100)}>Click Minus</button>
        </div>
    );
}
export default Counter;
```

## 1.4. Development based on `Django` (backend) and `React` （frontend)

### 1.4.1. Virtual Env

1. Use `pipenv`

Use `pipenv shell` in project folder to launch (create) virtual env, which allows us to install dependencies and packages only inside the project

also use `exit` to exit virtual env anything we need.

```bash
pipenv shell
```

### 1.4.2. Back-End

2. Install Django Rest Framework (a toolkit to build api)

```bash
pipenv install djangorestframework
```

3. Install Django Cors Header (allow api to be accessed on any other domain)

```bash
pipenv install django-cors-headers
```

4. `serializer`

To create api in django project we need to create a `serializer.py` file, which a used to convert complex data to nactive python data types, then be easily rendered into json.

### 1.4.3. Front-End

5. React app

```bash
npx create-react-app frontend #name of application
```

6. `reactstrap` & `bootstrap`
   In fontend folder

```
npm install reactstrap bootstrap
```

### 1.4.4. Connecting Back-End(Django) to Front-End(React) using [Axios](https://axios-http.com/docs/intro)

A Axios installed in frontend folder to connect back-end and front-end

```bash
npm install axios # install for react (in fontend folder)
```

### 1.4.5. Setting for interaction between Django and React

Connect backend server which will be written in django framework to our front-end which will be written in React.

In `setting.py`, we need to add some variable as configuration to allow interaction between `django` and `react`:

```py
# Application definition

INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework'
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
]
...

REST_FRAMEWORK = {'DEFAULT_PERMISSION_CLASSES': [
   'rest_framework.permissions.AllowAny',
]}

CORS_ORIGIN_ALLOW_ALL = True

# WhiteListing React port
CORS_ORIGIN_WHITELIST = ('http://localhost:3000')
```

In django app, we need to create `serializer.py` which is to convert the model instances (define in `models.py`) to `json` data (**`json` is the standard for data interchange on the web**)

## 1.5. Practice - Task Manager

### 1.5.1. Project Structure

1. **Back-End:** Django + pipenv packages (django rest framework + django cors headers)
2. **Front-End:** React + npm packages (reactstrap + boostrap + axios)
