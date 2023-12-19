<template>
    <div ref="container" class="container">{{ content }}</div>
    <input type="text" ref="username">
    <button @click="getElementHandle">获取元素</button>
</template>
/** 在vue中对DOM的基本操作
 * 内容改变： {{ 模板语法 }}
 * 属性改变： v-bind: 指令
 * 事件: v-on:
 * 如果没有特别的需求，不要操作DOM
 */
<script>
export default {
    data() {
        return {
            content:"content"
        };
    },
    methods: {
        getElementHandle() {
            console.log(this.$refs.container)
            console.log(this.$refs.container.innerHTML = 'asdas')
            // this.content = "tuqioq"
            console.log(this.$refs.username.value)
        }
    }
}
</script>