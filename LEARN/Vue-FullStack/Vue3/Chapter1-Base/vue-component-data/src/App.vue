<template>
    <h3>App</h3>
    <Parent />
</template>
<script>
import { computed } from "vue";
import Parent from "./components/Parent.vue";
export default {
    data() {
        return {
            message: "Applicn Data",
        };
    },
    components: {
        Parent,
    },
    // provide: {
    //     message: "App Data",
    // },
    // provide() {
    //     return {
    //         message: computed(() => this.message),
    //     };
    // },
    provide() {
        return {
            message: this.message,
        };
    },
};
</script>
