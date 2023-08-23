import { createStore } from "vuex";

export default createStore({
    // define global state variables for each page
    state: {
        isLoading: false,
        isAuthenticated: false,
        token: "",
        user: {
            id: 0,
            username: "",
        },
        team: {
            id: 0,
            name: "",
            plan: "",
            max_leads: 0,
            max_clients: 0,
        },
        member: {
            id: 0,
            username: "",
            first_name: "",
            last_name: "",
        },
    },
    getters: {},
    // define operations to change states
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem("token")) {
                // setToken(state, localStorage.getItem("token"));
                state.token = localStorage.getItem("token");
                state.isAuthenticated = true;
                state.user.id = localStorage.getItem("userid");
                state.user.username = localStorage.getItem("username");
                state.team.id = localStorage.getItem("team_id");
                state.team.name = localStorage.getItem("team_name");
                state.team.plan = localStorage.getItem("team_plan");
                state.team.max_leads = localStorage.getItem("team_max_leads");
                state.team.max_clients =
                    localStorage.getItem("team_max_clients");
            } else {
                // removeToken(state);
                state.token = "";
                state.isAuthenticated = false;
                state.user.id = 0;
                state.user.username = "";
                state.team.id = 0;
                state.team.name = "";
                state.team.plan = "";
                state.team.max_leads = 0;
                state.team.max_clients = 0;
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

        setUser(state, user) {
            state.user = user;
        },
        setTeam(state, team) {
            state.team = team;
            localStorage.setItem("team_id", team.id);
            localStorage.setItem("team_name", team.name);
            localStorage.setItem("team_plan", team.plan);
            localStorage.setItem("team_max_leads", team.max_leads);
            localStorage.setItem("team_max_clients", team.max_clients);
        },
        setMember(state, member) {
            state.member = member;
            localStorage.setItem("member_id", member.id);
            localStorage.setItem("member_username", member.username);
            localStorage.setItem("member_first_name", member.first_name);
            localStorage.setItem("member_last_name", member.last_name);
        },
    },
    actions: {},
    modules: {},
});
