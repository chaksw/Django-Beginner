<template>
    <!-- <SlotsBase>
        <div>
            <h3>Slots Title</h3>
            <p>Slots Contents</p>
        </div>
    </SlotsBase> -->
    <!-- <SlotsRenderScope> -->
    <!-- 引用父组件变量 -->
    <!-- <template #header> -->
    <!-- <h3>{{ title }}</h3> -->
    <!-- </template> -->
    <!-- <template #main> -->
    <!-- <p>{{ content }}</p> -->
    <!-- </template> -->
    <!-- </SlotsRenderScope> -->
    <SlotsAttr>
        <template #header="slotProps">
            <p>{{ content }}</p>
            <p>{{ slotProps.msg }}</p>
        </template>
        <template #main="slotProps">
            <p>{{ slotProps.job }}</p>
        </template>
    </SlotsAttr>
</template>
<script>
import SlotsBase from "./components/SlotsBase.vue";
import SlotsRenderScope from "./components/SlotsRenderScope.vue";
import SlotsAttr from "./components/SlotsAttr.vue";
export default {
    data() {
        return {
            title: "Slot Title",
            content: "Slot Content",
        };
    },
    components: {
        SlotsBase,
        SlotsRenderScope,
        SlotsAttr,
    },
};
</script>
