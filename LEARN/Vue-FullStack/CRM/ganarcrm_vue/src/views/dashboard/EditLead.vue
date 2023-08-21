<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{ lead.company }}</h1>
            </div>
            <div class="column is-10">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="company">Company</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="company"
                                v-model="lead.company" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="contact_person">Contact Person</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="contact_person"
                                v-model="lead.contact_person" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="email">Email</label>
                        <div class="contorl">
                            <input
                                type="email"
                                class="input"
                                id="email"
                                v-model="lead.email" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="phone">Phone</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="phone"
                                v-model="lead.phone" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="website">Website</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="website"
                                v-model="lead.website" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="confidence">Confidence</label>
                        <div class="contorl">
                            <input
                                type="number"
                                class="input"
                                id="confidence"
                                v-model="lead.confidence" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="estimated_value">Estimated Value</label>
                        <div class="contorl">
                            <input
                                type="number"
                                class="input"
                                id="estimated_value"
                                v-model="lead.estimated_value" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="status">Status</label>
                        <div class="control">
                            <div class="select">
                                <select id="status" v-model="lead.status">
                                    <option value="new">New</option>
                                    <option value="contacted">Contacted</option>
                                    <option value="inprogress">
                                        In progress
                                    </option>
                                    <option value="lost">Lost</option>
                                    <option value="won">Won</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="field">
                        <label for="">Priority</label>
                        <div class="control">
                            <div class="select">
                                <select id="priority" v-model="lead.priority">
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <label for="">Assigned to</label>
                        <div class="control">
                            <div class="select">
                                <select
                                    id="assigned_to"
                                    v-model="lead.assigned_to">
                                    <option value="" selected>
                                        Select member
                                    </option>
                                    <option
                                        v-for="member in team.members"
                                        v-bind:id="member.id"
                                        v-bind:value="member.id">
                                        {{ member.username }}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success" type="submit">
                                Update
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
    name: "EditLead",
    data() {
        return {
            lead: {},
            team: {
                members: [],
            },
        };
    },
    mounted() {
        this.getLead();
        this.getTeam();
    },
    methods: {
        async getLead() {
            this.$store.commit("setIsLoading", true);

            const leadID = this.$route.params.id;
            await axios
                .get(`api/v1/leads/${leadID}`)
                .then((response) => {
                    console.log(response);
                    this.lead = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
        async getTeam() {
            this.$store.commit("setIsLoading", true);
            await axios
                .get("api/v1/teams/get_my_team/")
                .then((response) => {
                    console.log(response.data);
                    this.team = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
        async submitForm() {
            const leadID = this.$route.params.id;
            this.$store.commit("setIsLoading", true);
            await axios
                .patch(`/api/v1/leads/${leadID}/`, this.lead)
                .then((response) => {
                    toast({
                        message: "The Lead was updated sucessfully",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    // this.$router.push(`/dashboard/leads/${leadID}/`);
                    this.$router.push({
                        name: "Lead",
                        params: { id: leadID },
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
