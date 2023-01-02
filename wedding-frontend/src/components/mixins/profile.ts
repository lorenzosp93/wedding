import { useAuthStore } from "@/stores";
import { mapActions, mapState } from "pinia";
import { defineComponent } from "vue";

export default defineComponent({
  computed: {
    ...mapState(useAuthStore, ["profile"]),
  },
  methods: {
    ...mapActions(useAuthStore, ["login", "logout"]),
  },
});
