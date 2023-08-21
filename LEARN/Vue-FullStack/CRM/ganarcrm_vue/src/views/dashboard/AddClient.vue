<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add client</h1>
            </div>
            <div class="column is-10">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="company">Name</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="name"
                                v-model="name" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="contact_person">Contact Person</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="contact_person"
                                v-model="contact_person" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="email">Email</label>
                        <div class="contorl">
                            <input
                                type="email"
                                class="input"
                                id="email"
                                v-model="email" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="phone">Phone</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="phone"
                                v-model="phone" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="website">Website</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="website"
                                v-model="website" />
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success" type="submit">
                                Submit
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
            name: "",
            contact_person: "",
            email: "",
            phone: "",
            website: "",
            errors: [],
        };
    },
    methods: {
        async submitForm() {
            console.log("submit");
            this.$store.commit("setIsLoading", true);
            const client = {
                name: this.name,
                contact_person: this.contact_person,
                email: this.email,
                phone: this.phone,
                website: this.website,
            };
            await axios
                .post("/api/v1/clients/", client)
                .then((response) => {
                    console.log(response);
                    toast({
                        message: "The Client was created sucessfully",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    // this.$router.push("/dashboard/clients/");
                    this.$router.push({ name: "Clients" });
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
