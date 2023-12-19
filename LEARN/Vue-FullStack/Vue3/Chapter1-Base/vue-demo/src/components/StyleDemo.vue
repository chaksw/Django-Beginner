<!-- Style Binding -->
<template>
    <p :style="{ color: activeColor, fontSize: fontSize + 'px' }">
        Style Binding 1
    </p>
    <p :style="styleObject">Style Binding 2</p>
</template>
<script>
export default {
    data() {
        return {
            activeColor: "green",
            fontSize: 30,
            styleObject: {
                color: "red",
                fontSize: "30px",
            },
        };
    },
};
</script>
