<template>
    <h3>Evnet Modifiers</h3>
    <a @click.prevent="clickHandle" href="http://www.google.com">Google</a>
    <div @click="clickDiv">
        <p @click.stop="clickP">测试冒泡</p>
    </div>
</template>

<script>
export default {
    data() {
        return {};
    },
    methods: {
        clickHandle(e) {
            // 阻止默认事件
            // e.preventDefault();
            console.log("Clicked but default action is prevented");
        },
        clickDiv() {
            console.log("DIV clicked");
        },
        clickP() {
            console.log("P clicked");
        },
    },
};
</script>
