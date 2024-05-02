module.exports = {
  parserOptions: {
    ecmaVersion: 2020
  },
  root: true,
  env: {
    node: true
  },
  extends: ['plugin:vue/vue3-recommended', '@vue/eslint-config-standard'],
  rules: {
    'vue/no-v-html': 'off',
    'no-unused-vars': 'error',
    'no-constant-condition': 'warn',
    'vue/no-side-effects-in-computed-properties': 'warn',
    'vue/no-unused-components': 'warn',
    'vue/no-mutating-props': 'warn',
    'no-console': 'off',
    'vue/v-on-event-hyphenation': 'off',
    'no-return-await': 'off',
    'vue/multi-word-component-names': 'off',
    'vue/no-reserved-component-names': 'off'
  }
}
