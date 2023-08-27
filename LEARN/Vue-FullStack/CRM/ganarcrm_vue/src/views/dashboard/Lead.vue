<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">{{ lead.company }}</h1>
                <div class="buttons">
                    <router-link
                        :to="{ name: 'EditLead', params: lead.id }"
                        class="button is-primary">
                        Edit
                    </router-link>
                    <button
                        @click="convert_lead_to_client"
                        class="button is-info">
                        Convert to client
                    </button>
                    <button class="button is-danger" @click="deleteLead">
                        Delete
                    </button>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Detail</h2>
                    <template v-if="lead.assigned_to">
                        <p>
                            <strong>Assigned to:</strong>
                            {{ lead.assigned_to.first_name }}
                            {{ lead.assigned_to.last_name }}
                        </p>
                    </template>
                    <p>
                        <strong>Status:</strong>
                        {{ lead.status }}
                    </p>
                    <p>
                        <strong>Priority:</strong>
                        {{ lead.priority }}
                    </p>
                    <p>
                        <strong>Confidence:</strong>
                        {{ lead.confidence }}
                    </p>
                    <p>
                        <strong>Estimated value:</strong>
                        {{ lead.estimated_value }}
                    </p>

                    <p>
                        <strong>Created at:</strong>
                        {{ lead.created_at }}
                    </p>
                    <p>
                        <strong>Modified at:</strong>
                        {{ lead.modified_at }}
                    </p>
                </div>
            </div>
            <div class="column is-6">
                <div class="box">
                    <h2 class="subtitle">Contact information</h2>
                    <p>
                        <strong>Contact person:</strong>
                        {{ lead.contact_person }}
                    </p>
                    <p>
                        <strong>Email:</strong>
                        {{ lead.email }}
                    </p>
                    <p>
                        <strong>Phone:</strong>
                        {{ lead.phone }}
                    </p>
                    <p>
                        <strong>Website:</strong>
                        {{ lead.website }}
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
    name: "Lead",
    data() {
        return {
            lead: {},
        };
    },
    mounted() {
        this.getLead();
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
        async convert_lead_to_client() {
            this.$store.commit("setIsLoading", true);

            const leadID = this.$route.params.id;
            const data = {
                lead_id: leadID,
            };
            await axios
                .post(`api/v1/convert_lead_to_client/`, data)
                .then((response) => {
                    console.log("concerted to client");
                    this.$router.push({ name: "Clients" });
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
        async deleteLead() {
            this.$store.commit("setIsLoading", true);

            const leadID = this.$route.params.id;

            await axios
                .post(`api/v1/leads/delete_lead/${leadID}`)
                .then((response) => {
                    console.log(response.data);
                    toast({
                        message: "The Lead was deleted",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    this.$router.push({ name: "Leads" });
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
