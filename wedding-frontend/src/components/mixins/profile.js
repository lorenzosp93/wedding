import { useAuthStore } from '@/stores';
import { mapActions, mapState } from 'pinia';

export default {
    data () {
        return {
        }
    },
    computed: {
    ...mapState(useAuthStore, ['profile', 'languages'])
    },
    methods: {
    ...mapActions(useAuthStore, [
        'login',
        'logout',
        'updateLanguage'
    ])
    },
}