<template>
    <h3>Slots Attribute</h3>
    <slot name="header" :msg="childMessage"></slot>
    <slot name="main" :job="job"></slot>
</template>
<script>
export default {
    data() {
        return {
            childMessage: "Child Component Data",
            job: "Software Engr",
        };
    },
};
</script>
