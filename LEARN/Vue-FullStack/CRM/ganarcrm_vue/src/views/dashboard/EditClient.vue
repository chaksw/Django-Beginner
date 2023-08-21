<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit {{ client.name }}</h1>
            </div>
            <div class="column is-10">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="name">Name</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="name"
                                v-model="client.name" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="contact_person">Contact Person</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="contact_person"
                                v-model="client.contact_person" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="email">Email</label>
                        <div class="contorl">
                            <input
                                type="email"
                                class="input"
                                id="email"
                                v-model="client.email" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="phone">Phone</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="phone"
                                v-model="client.phone" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="website">Website</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="website"
                                v-model="client.website" />
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
    name: "AddClient",
    data() {
        return {
            client: {},
        };
    },
    mounted() {
        this.getClient();
    },
    methods: {
        async getClient() {
            this.$store.commit("setIsLoading", true);

            const clientID = this.$route.params.id;
            await axios
                .get(`api/v1/clients/${clientID}`)
                .then((response) => {
                    console.log(response);
                    this.client = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
        async submitForm() {
            const clientID = this.$route.params.id;
            this.$store.commit("setIsLoading", true);
            await axios
                .patch(`/api/v1/clients/${clientID}/`, this.client)
                .then((response) => {
                    toast({
                        message: "The client was updated sucessfully",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    // this.$router.push(`/dashboard/clients/${clientID}/`);
                    this.$router.push({
                        name: "Client", // name | component of router in routes{}
                        params: { id: clientID },
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
