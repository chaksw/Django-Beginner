<template>
    <h3>Template Syntax</h3>
    <p>{{ msg }}</p>
    <p>{{ hello }}</p>
    <p>{{ number + 1 }}</p>
    <p>{{ ok ? "Yes" : "No" }}</p>
    <p>{{ message.split("").reverse().join("") }}</p>
    <p>{{ rawHtml }}</p>
    <p><span v-html="rawHtml"></span></p>
</template>
<script>
export default {
    data() {
        return {
            msg: "神奇的语法",
            hello: "hello world",
            number: 10,
            ok: true,
            message: "大家好",
            rawHtml: "<a href='https://www.google.com'>Google</a>",
        };
    },
};
</script>
