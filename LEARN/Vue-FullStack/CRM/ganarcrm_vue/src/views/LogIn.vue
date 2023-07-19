<template>
    <div class="container">
        <div class="culumns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form action="">
                    <div class="field">
                        <label for="email">Email</label>
                        <div class="control">
                            <input
                                type="email"
                                class="input"
                                name="email"
                                id="email" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="password1">Password</label>
                        <div class="control">
                            <input
                                type="password"
                                class="input"
                                name="password1"
                                id="password1" />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "LogIn",
};
</script>
