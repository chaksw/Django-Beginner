<template>
    <h3>Component Lifecycle application</h3>
    <p ref="name">Data</p>
    <ul>
        <li v-for="(item, index) in banner" :key="index">
            <h3>{{ item.name }}</h3>
            <p>{{ item.age }}</p>
            <p>{{ item.secretIdentity }}</p>
        </li>
    </ul>
</template>

<script>
export default {
    data() {
        return {
            banner: [],
        };
    },
    // 不可行，在组件创建之前初始化 data()不存在
    beforeCreate() {
        // 模拟网络请求
        this.banner = [
            {
                name: "Molecule Man",
                age: 29,
                secretIdentity: "Dan Jukes",
            },
            {
                name: "Madame Uppercut",
                age: 39,
                secretIdentity: "Jane Wilson",
            },
            {
                name: "Eternal Flame",
                age: 1000000,
                secretIdentity: "Unknown",
            },
        ];
    },
    // 可以实现模拟网络请求，但此时UI渲染还未加载完成
    created() {
        // 模拟网络请求
        // this.banner = [
        //     {
        //         name: "Molecule Man",
        //         age: 29,
        //         secretIdentity: "Dan Jukes",
        //     },
        //     {
        //         name: "Madame Uppercut",
        //         age: 39,
        //         secretIdentity: "Jane Wilson",
        //     },
        //     {
        //         name: "Eternal Flame",
        //         age: 1000000,
        //         secretIdentity: "Unknown",
        //     },
        // ];
    },
    beforeMount() {
        console.log(this.$refs.name); // undefined
    },
    // 最好的情况：先完成渲染结构，再请求数据
    mounted() {
        console.log(this.$refs.name);
        // 模拟网络请求
        this.banner = [
            {
                name: "Molecule Man",
                age: 29,
                secretIdentity: "Dan Jukes",
            },
            {
                name: "Madame Uppercut",
                age: 39,
                secretIdentity: "Jane Wilson",
            },
            {
                name: "Eternal Flame",
                age: 1000000,
                secretIdentity: "Unknown",
            },
        ];
    },
};
</script>
