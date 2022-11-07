import { useAuthStore } from '@/stores';
import { mapActions, mapState } from 'pinia';

export default {
    data () {
        return {
        }
    },
    computed: {
    ...mapState(useAuthStore, ['profile'])
    },
    methods: {
    ...mapActions(useAuthStore, [
        'login',
        'logout'
    ])
    },
}