<template>
    <h3>Slots Render Scope</h3>
    <slot name="header">
        <!-- fallback content -->
        <p>FallBack Content1</p>
    </slot>
    <hr />
    <slot name="main">
        <!-- fallback content -->
        <p>FallBack Content2</p>
    </slot>
</template>
<script>
export default {
    data() {
        return {};
    },
};
</script>
