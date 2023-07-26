<template>
    <nav class="navbar is-black">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Ganr CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <router-link to="/dashboard/leads/" class="navbar-item">
                    Leads
                </router-link>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link
                                class="button is-success"
                                to="/sign-up">
                                <strong>Sign Up</strong>
                            </router-link>
                            <router-link class="button" to="/log-in">
                                Log in
                            </router-link>
                        </template>
                        <template v-else>
                            <router-link
                                class="button is-info"
                                to="/dashboard/my-account">
                                My Account
                            </router-link>
                        </template>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: "NavBar",
};
</script>
