import { createRouter, createWebHistory } from "vue-router";
import store from "../store";
import HomeView from "../views/HomeView.vue";
import SignUp from "../views/SignUp.vue";
import LogIn from "../views/LogIn.vue";
import Dashboard from "../views/dashboard/Dashboard.vue";
import MyAccount from "../views/dashboard/MyAccount.vue";
const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/about",
        name: "about",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
    },
    {
        path: "/sign-up",
        name: "SignUp",
        component: SignUp,
        meta: {
            requireLogin: false,
        },
    },
    {
        path: "/log-in",
        name: "LogIn",
        component: LogIn,
        meta: {
            requireLogin: false,
        },
    },
    {
        path: "/dashboard",
        name: "Dashboard",
        component: Dashboard,
        meta: {
            requireLogin: true,
        },
    },
    {
        path: "/dashboard/my-account",
        name: "MyAccount",
        component: MyAccount,
        meta: {
            requireLogin: true,
        },
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});
// Navigation Guard
router.beforeEach((to, from, next) => {
    // if url need to go require log in and user is not anthenticated, go back to login page
    if (
        to.matched.some((record) => record.meta.requireLogin) &&
        !store.state.isAuthenticated
    ) {
        next("/log-in");
    } else {
        next();
    }
});
export default router;
