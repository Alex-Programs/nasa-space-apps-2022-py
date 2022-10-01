<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

.box {
    border: 2px solid rgba(255, 255, 255, 0.2);
    background-color: rgba(255, 255, 255, 0.2);
}
</style>

<div class="py-64 px-16 box rounded-3xl mb-8" >
    <slot />
</div>