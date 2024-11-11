<template>
    <div class="content_heder">
        <h4 class="type">{{ title }}</h4>
        <a v-if="isShowLink" :href="link">Xem thêm</a>
    </div>
</template>

<script setup lang="ts">
const props = defineProps<{
    title: string;
    link: string;
    isShowLink: boolean;
}>();
</script>

<style lang="css" scoped>
.type {
    margin: 0;
}

.content_heder {
    background: linear-gradient(90deg, var(--color-primary) 0%, #001815 100%) 0%
        0% no-repeat;
    padding: 10px;
    margin: 8px 0;
    color: #fff;
    text-transform: uppercase;
    display: flex;
    justify-content: space-between;
}

a {
    color: #fff;
}
</style>
