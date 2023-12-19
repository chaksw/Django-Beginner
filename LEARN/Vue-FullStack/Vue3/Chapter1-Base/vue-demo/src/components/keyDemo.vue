<!-- Status Management through key -->
<template>
    <h3>v-for Status Management by key</h3>
    <p v-for="(item, index) in names" :key="index">{{ index }}-{{ item }}</p>
    <div v-for="item in results" :key="item.id">
        <p>{{ item.title }}</p>
        <img  class='imgsize' :src="item.avator" :alt="item.id" />
    </div>
</template>
<script>
export default {
    data() {
        return {
            names: ["Chris", "Lyrics", "Murphy"],
            results: [
            {
                    id: 2261677,
                    title: "鄂尔多斯｜感受一座城市的璀璨夜景 感受一座城市，除了白日里的车水马龙，喧嚣繁华之",
                    avator: "https://mma.prnewswire.com/media/1420781/Honeywell_Logo.jpg?p=publish",
                },
                {
                    id: 2261566,
                    title: "成都这家洞穴暗黑风咖啡厅酷毙了！！早C晚A走起☕️ 成都天气这么🔥 咖啡🌟人必备",
                    avator: "https://mma.prnewswire.com/media/1420781/Honeywell_Logo.jpg?p=publish",
                },
                {
                    id: 2261662,
                    title: "[川西新龙-措卡湖]措卡湖吗，意为“乱世从中的黑色海水”，神秘小众 原汁原味。",
                    avator: "https://mma.prnewswire.com/media/1420781/Honeywell_Logo.jpg?p=publish",
                },
            ],
        };
    },
};
</script>

<style>
.imgsize{
    width: 250px;
}
</style>
