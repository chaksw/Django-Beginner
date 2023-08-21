<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add lead</h1>
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
                                v-model="company" />
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
                        <label for="confidence">Confidence</label>
                        <div class="contorl">
                            <input
                                type="number"
                                class="input"
                                id="confidence"
                                v-model="confidence" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="estimated_value">Estimated Value</label>
                        <div class="contorl">
                            <input
                                type="number"
                                class="input"
                                id="estimated_value"
                                v-model="estimated_value" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="status">Status</label>
                        <div class="control">
                            <div class="select">
                                <select id="status" v-model="status">
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
                                <select id="priority" v-model="priority">
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                            </div>
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
    name: "AddLead",
    data() {
        return {
            company: "",
            contact_person: "",
            email: "",
            phone: "",
            website: "",
            confidence: 0,
            estimated_value: 0,
            status: "new",
            priority: "medium",

            errors: [],
        };
    },
    methods: {
        async submitForm() {
            console.log("submit");
            this.$store.commit("setIsLoading", true);
            const lead = {
                company: this.company,
                contact_person: this.contact_person,
                email: this.email,
                phone: this.phone,
                website: this.website,
                confidence: this.confidence,
                estimated_value: this.estimated_value,
                status: this.status,
                priority: this.priority,
            };
            await axios
                .post("/api/v1/leads/", lead)
                .then((response) => {
                    console.log(response);
                    toast({
                        message: "The Lead was created sucessfully",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    // this.$router.push("/dashboard/leads/");
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
