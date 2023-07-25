<template>
    <div class="container">
        <div class="culumns is-multiline">
            <div class="column is-12">
                <h1 class="title">Leads</h1>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Leads",
    data() {
        return {
            leads: [],
        };
    },
    mounted() {
        this.getLeads();
    },
    methods: {
        async getLeads() {
            this.$store.commit("setIsLoading", true);

            axios
                .get("/api/v1/leads/")
                .then((response) => {
                    console.log(response.data);
                    this.leads = response.data;
                    console.log(this.leads);
                })
                .catch((error) => {
                    console.log(error);
                });

            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
