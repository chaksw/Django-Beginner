<!-- Array Change Watchers -->
<template>
    <h3>Array Change Watchers</h3>
    <p v-for="(item, index) in names" :key="index"></p>
    <button @click="addLikstHandle">Add Data</button>
    <ul>
        <li v-for="(item, index) in names" :key="index">
            {{ item }}
        </li>
    </ul>
    <button @click="ConcatHandle">Concat Array</button>
    <h3>Array 1</h3>
    <p v-for="(item, index) in nums1" :key="index">{{ item }}</p>
    <h3>Array 2</h3>
    <p v-for="(item, index) in nums2" :key="index">{{ item }}</p>
</template>

<script>
export default {
    data() {
        return {
            names: ["iwen", "ime", "frank"],
            nums1: [1, 2, 3, 4, 5],
            nums2: [6, 7, 8, 9, 10],
        };
    },
    methods: {
        addLikstHandle() {
            // 引起UI自动更新
            this.names.push("sakura");
            // 不会引起UI自动更新;
            this.names.concat(["sakura"]); // concat会生成一个新的数组，原数组不会发生变化
            console.log(this.names);
            // 将concat生成的新数组赋给names, 引起UI更新;
            this.names = this.names.concat(["sakura"]);
        },
        ConcatHandle() {
            this.nums1 = this.nums1.concat(this.nums2);
        },
    },
};
</script>
