export default {
    data () {
        return {
        }
    },
    methods: {
        removeHtml (value) {
        const div = document.createElement('div')
        div.innerHTML = value
        const text = div.textContent || div.innerText || ''
        return text
        },
        truncate (value, length) {
        if (!value) return "";
        value = value.toString();
        if (value.length > length) {
            return value.substring(0, length) + "...";
        } else {
            return value;
        }
        },
        formattedDate (date) {
        date = new Date(date);
        const yyyy = date.getYear() + 1900;
        const mm = date.getMonth() + 1;
        const dd = date.getDate();
        return `${yyyy}.${mm}.${dd}`
        },
    },
}