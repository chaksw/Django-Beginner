<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Plans</h1>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Free</h2>
                    <h4 class="is-size-3">$0</h4>
                    <p>Max 5 clients</p>
                    <p>Max 5 leads</p>
                    <button
                        @click="subscribe('Free')"
                        class="button is-primary mt-2">
                        Subscribe
                    </button>
                </div>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Small team</h2>
                    <h4 class="is-size-3">$10</h4>
                    <p>Max 15 clients</p>
                    <p>Max 15 leads</p>
                    <button
                        @click="subscribe('smallTeam')"
                        class="button is-primary mt-2">
                        Subscribe
                    </button>
                </div>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Big Team</h2>
                    <h4 class="is-size-3">$25</h4>
                    <p>Max 50 clients</p>
                    <p>Max 50 leads</p>
                    <button
                        @click="subscribe('bigTeam')"
                        class="button is-primary mt-2">
                        Subscribe
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
    name: "Plans",
    data() {
        return {};
    },
    mounted() {},
    methods: {
        async subscribe(plantype) {
            this.$store.commit("setIsLoading", true);
            const data = {
                plan: plantype,
            };
            await axios
                .post(`api/v1/teams/upgrade_plan/`, data)
                .then((response) => {
                    // set the upgraded teams data in back-end to front-end after POST
                    console.log("Upgraded data");
                    console.log(response.data);
                    this.$store.commit("setTeam", {
                        id: response.data.id,
                        name: response.data.name,
                        plan: response.data.plan.name,
                        max_leads: response.data.plan.max_leads,
                        max_clients: response.data.plan.max_clients,
                    });
                    toast({
                        message: "The Plan was upgraded sucessfully",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    // localStorage.setItem("team_name", response.data.username);
                    // localStorage.setItem("team_id", response.data.id);
                    // this.$router.push("dashboard/my-account");
                    this.$router.push({
                        name: "Team",
                    });
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
