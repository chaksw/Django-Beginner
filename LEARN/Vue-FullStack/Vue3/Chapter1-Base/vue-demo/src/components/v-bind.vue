<!-- Attribute Bindings v-bind -->
<template>
    <div :id="dynamicId" :class="dynamicClass" :title="dynamicTitle">Test</div>
    <div v-bind="objectOfAttrs">Multiple Attributes Binding</div>
    <button :disabled="isButtonDisabled">Button</button>
</template>

<script>
export default {
    data() {
        return {
            dynamicClass: "appClass",
            dynamicId: "appID",
            dynamicTitle: 'Hello',
            isButtonDisabled: false,
            objectOfAttrs: {
                id: "container",
                class: "appClass",
            },
        };
    },
};
</script>

<style>
.appClass {
    color: red;
    font-size: 30px;
}
</style>
