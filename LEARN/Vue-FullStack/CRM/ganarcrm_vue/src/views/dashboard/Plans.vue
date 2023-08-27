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
            <hr />
            <div class="column is-12">
                <button @click="cancelPlan()" class="button is-danger">
                    Cancel plan
                </button>
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
        return {
            pub_key: "",
            stripe: null,
        };
    },
    async mounted() {
        await this.getPubKey();
        this.stripe = Stripe(this.pub_key);
    },
    methods: {
        async getPubKey() {
            this.$store.commit("setIsLoading", true);
            await axios
                .get(`api/v1/stripe/get_stripe_pub_key/`)
                .then((response) => {
                    // console.log(response.data);
                    this.pub_key = response.data.pub_key;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
        async subscribe(plantype) {
            this.$store.commit("setIsLoading", true);
            const data = {
                plan: plantype,
            };

            await axios
                .post("/api/v1/stripe/create_checkout_session/", data)
                .then((response) => {
                    console.log(response);
                    return this.stripe.redirectToCheckout({
                        sessionId: response.data.sessionId,
                    });
                })
                .catch((error) => {
                    console.log("Error: ", error);
                });
            /* await axios
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
                });*/
            this.$store.commit("setIsLoading", false);
        },
        async cancelPlan() {
            this.$store.commit("setIsLoading", true);

            axios.post("/api/v1/teams/cancel_plan/").then((response) => {
                this.$store.commit("setTeam", {
                    id: response.data.id,
                    name: response.data.name,
                    plan: response.data.plan.name,
                    max_leads: response.data.plan.max_leads,
                    max_clients: response.data.plan.max_clients,
                });
                toast({
                    message: "The Plan was cancelled",
                    type: "is-success",
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: "bottom-right",
                });
                this.$router.push({
                    name: "Team",
                });
            });
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
