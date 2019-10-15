Vue.use(VueLoading);
Vue.component('loading', VueLoading)

Vue.component("step-navigation-step", {
    template: "#step-navigation-step-template",

    props: ["step", "currentstep"],

    computed: {
        indicatorclass() {
            return {
                active: this.step.id == this.currentstep,
                complete: this.currentstep > this.step.id
            };
        }
    }
});

Vue.component("step-navigation", {
    template: "#step-navigation-template",

    props: ["steps", "currentstep"]
});

Vue.component("step", {
    template: "#step-template",

    props: ["step", "stepcount", "currentstep"],

    computed: {
        active() {
            return this.step.id == this.currentstep;
        },

        firststep() {
            return this.currentstep == 1;
        },

        laststep() {
            return this.currentstep == this.stepcount;
        },

        stepWrapperClass() {
            return { active: this.active };
        }
    },

    methods: {
        stepValid() {
            const fields = document.getElementsByClassName('step-' + this.currentstep);
            for (let f of fields) {
                if (! f.checkValidity()) {
                    return false;
                }
            }
            return true;
        },

        submitForm() {
            this.showLoader();
            document.forms[0].submit();
        },

        showLoader() {
            let loader = this.$loading.show({
                loader: 'bars',
            });
        },

        nextStep() {
            if (this.stepValid()) {
                this.$emit("step-change", this.currentstep + 1);
            }
        },

        lastStep() {
            this.$emit("step-change", this.currentstep - 1);
        }
    }
});

new Vue({
    el: "#app",

    data: {
        currentstep: 1,

        steps: [
            {
                id: 1,
                title: "Basic Info",
                icon_class: "fa fa-user-circle-o"
            },
            {
                id: 2,
                title: "Federal Income",
                icon_class: "fa fa-th-list"
            },
            {
                id: 3,
                title: "Federal Income Adjustments",
                icon_class: "fa fa-th-list"
            },
            {
                id: 4,
                title: "Business Income",
                icon_class: "fa fa-th-list"
            },
            {
                id: 5,
                title: "Federal Deductions",
                icon_class: "fa fa-th-list"
            },
            {
                id: 6,
                title: "Estimated Tax Payments",
                icon_class: "fa fa-paper-plane"
            }
        ]
    },

    methods: {
        stepChanged(step) {
            this.currentstep = step;
        }
    }
});
