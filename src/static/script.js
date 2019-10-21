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

            let stepValid = true;
            for (let f of fields) {
                if (f.reportValidity()) {
                    f.classList.add('is-valid');
                    f.classList.remove('is-invalid');
                } else {
                    stepValid = false;
                    f.classList.add('is-invalid');
                    f.classList.remove('is-valid');
                }
            }

            return stepValid;
        },

        nextStep() {
            if (this.stepValid()) {
                this.$emit("step-change", this.currentstep + 1);
            }
        },

        lastStep() {
            this.$emit("step-change", this.currentstep - 1);
        },

        submitForm() {
            if (this.stepValid()) {
                this.$loading.show({ loader: 'bars' })
                document.forms[0].submit();
            }
        },
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


const updateValidityIndicator = (event) => {
    const e = event.target;

    if (e.checkValidity()) {
        e.classList.add('is-valid');
        e.classList.remove('is-invalid');
    } else {
        e.classList.remove('is-valid');
        e.classList.add('is-invalid');
    }
}

for (let element of document.getElementsByTagName('input')) {
    element.addEventListener('blur', updateValidityIndicator);
    element.addEventListener('keyup', updateValidityIndicator);
}

for (let element of document.getElementsByTagName('select')) {
    element.addEventListener('blur', updateValidityIndicator);
}
