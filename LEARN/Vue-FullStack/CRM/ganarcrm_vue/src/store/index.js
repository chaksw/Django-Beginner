import { createStore } from "vuex";

export default createStore({
    // define global state variables
    state: {
        isLoading: false,
        isAuthenticated: false,
        token: "",
    },
    getters: {},
    // define opetions to change states
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("token")) {
                // setToken(state, localStorage.getItem("token"));
                state.token = localStorage.getItem("token");
                state.isAuthenticated = true;
            } else {
                // removeToken(state);
                state.token = "";
                state.isAuthenticated = false;
            }
        },
        setIsLoading(state, status) {
            state.isLoading = status;
        },
        setToken(state, token) {
            state.token = token;
            state.isAuthenticated = true;
        },
        removeToken(state) {
            state.token = "";
            state.isAuthenticated = false;
        },
    },
    actions: {},
    modules: {},
});
