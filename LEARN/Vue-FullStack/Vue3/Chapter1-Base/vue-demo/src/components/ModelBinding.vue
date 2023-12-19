<!-- Form input bindings v-model -->
<template>
    <!-- binding input -->
    <h3>Form Input Bindings</h3>
    <form action="">
        <p>Message is: {{ message }}</p>
        <input type="text" v-model="message" placeholder="edit me">
    </form>

    <form action="">
        <input type="checkbox" id="checkobx" value="Hey" v-model="checked" >
        <label for="checkobx">{{ checked }}</label>
    </form>
    <!-- binding textarea -->
    <form action="">
        <span>Multiline message is:</span>
        <p>{{ message1 }}</p>
        <textarea name="" id="" cols="50" rows="10" v-model="message1"></textarea>
    </form>
    <!-- binding checkbox to array or set, value will be send to checkedNamed once checkbox is set to true -->
    <form action="">
        <div>Checked names: {{ checkedNames }}</div>

        <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">
        <label for="jack">Jack</label>

        <input type="checkbox" id="john" value="John" v-model="checkedNames">
        <label for="john">John</label>

        <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">
        <label for="mike">Mike</label>

    </form>
    <!-- binding radio checkbox to array or set -->
    <form action="">
        <div>Picked: {{ picked }}</div>

        <input type="radio" id="one" value="One" v-model="picked" />
        <label for="one">One</label>

        <input type="radio" id="two" value="Two" v-model="picked" />
        <label for="two">Two</label>
    </form>
    <!-- binding select to array or set -->
    <form action="">
        <div>Selected: {{ selected }}</div>
        <select name="" id="" v-model="selected">
            <option disabled value="">Please select one</option>
            <option value="Apple">A</option>
            <option value="Bananas">B</option>
            <option value="Cat">C</option>
    
        </select>
    </form>
    <!-- Binding multiple select to array or set -->
    <form action="">
        <div>Multi-Selected: {{ selected1 }}</div>
        <select name="" id="" multiple v-model="selected1">
            <option value="Apple">A</option> 
            <option value="Bpple">B</option>
            <option value="Cpple">C</option>
        </select>
    </form>

    <!-- Rendering by v-for -->
    <form action="">
        <div>Selected: {{ selected2 }}</div>
        <select name="" id="" v-model="selected2">
            <option v-for="option in options" :value="option.value">
            {{ option.text }}
        </option></select>
        
    </form>

    <form action="">
        <h3>Lazy Form Input Bindings</h3>
        <input type="text" v-model.lazy="message2">
        <p>{{ message2 }}</p>
    </form>
</template>

<script>
export default {
    data() {
        return {
            message: '',
            message2: '',
            checked: true,
            message1: '',
            checkedNames: [],
            picked: [],
            selected: [],
            selected1: [],
            selected2: 'A',
            options: [
                {text: 'One', value: 'A'},
                {text: 'Two', value: 'B'},
                {text: 'Three', value: 'C'},
                {text: ' asd', value: '613'}
            ]
        };
    },
    methods:{
            
        }
}
    
</script>