<template>
    <nav class="navbar is-gray">
        <div class="navbar-brand">
            <router-link to="/" class="navbar-item">
                <strong>Ganr CRM</strong>
            </router-link>
        </div>

        <div class="navbar-menu">
            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <router-link class="button is-success" to="/sign-up">
                            <strong>Sign Up</strong>
                        </router-link>
                        <router-link class="button" to="/log-in">
                            Log in
                        </router-link>
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
