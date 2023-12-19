<script>
// 1. import component
import ArrtibBinding from "./components/ArrtibBinding.vue";
import IfDemo from "./components/IfDemo.vue";
import ListDemo from "./components/ListDemo.vue";
import KeyDemo from "./components/KeyDemo.vue";
import EventDemo1 from "./components/EventDemo1.vue";
import EventDemo2 from "./components/EventDemo2.vue";
import EventDemo3 from "./components/EventDemo3..vue";
import EventDemo4 from "./components/EventDemo4.vue";
import EventDemo5 from "./components/EventDemo5.vue";
import EventDemo6 from "./components/EventDemo6.vue";
import ArrayList from "./components/ArrayList.vue";
import ComputedDemo from "./components/ComputedDemo.vue";
import ClassDemo from "./components/ClassDemo.vue";
import StyleDemo from "./components/StyleDemo.vue";
import WatchersDemo from "./components/WatchersDemo.vue";
import ModelBinding from "./components/ModelBinding.vue";
import TemplateRefs from "./components/TemplateRefs.vue";
import ComponentBasic from "./components/ComponentBasic.vue";

export default {
    // 2. injection of component
    components: {
        ComponentBasic
    }
}

</script>

<template>
    <!-- 3. display component -->
    <!-- <ArrtibBinding /> -->
    <!-- <IfDemo /> -->
    <!-- <ListDemo /> -->
    <!-- <KeyDemo /> -->
    <!-- <EventDemo1 /> -->
    <!-- <EventDemo2 /> -->
    <!-- <EventDemo3 /> -->
    <!-- <EventDemo4 /> -->
    <!-- <EventDemo5 /> -->
    <!-- <EventDemo6 /> -->
    <!-- <ArrayList /> -->
    <!-- <ComputedDemo /> -->
    <!-- <ClassDemo /> -->
    <!-- <StyleDemo /> -->
    <!-- <WatchersDemo /> -->
    <!-- <ModelBinding /> -->
    <!-- <TemplateRefs/> -->
    <ComponentBasic/>
    <component-basic/>
</template>
