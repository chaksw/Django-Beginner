<template>
    <nav class="navbar is-black">
        <div class="navbar-brand">
            <router-link :to="{ name: 'home' }" class="navbar-item">
                <strong>Ganr CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <template v-if="$store.state.isAuthenticated">
                    <router-link :to="{ name: 'Leads' }" class="navbar-item">
                        Leads
                    </router-link>
                    <router-link :to="{ name: 'Clients' }" class="navbar-item">
                        Clients
                    </router-link>
                    <router-link :to="{ name: 'Team' }" class="navbar-item">
                        Team
                    </router-link>
                </template>
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="!$store.state.isAuthenticated">
                            <router-link
                                class="button is-success"
                                :to="{ name: 'SignUp' }">
                                <strong>Sign Up</strong>
                            </router-link>
                            <router-link class="button" :to="{ name: 'LogIn' }">
                                Log in
                            </router-link>
                        </template>
                        <template v-else>
                            <router-link
                                class="button is-info"
                                :to="{ name: 'MyAccount' }">
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
