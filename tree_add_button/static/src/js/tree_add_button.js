openerp.tree_add_button = function(instance) {
var QWeb = instance.web.qweb,
        _t = instance.web._t,
        _lt = instance.web._lt;
        /**
          * 导出模板
          * */   

instance.web.ListView.include({
        init: function() {
            var self = this;
            this._super.apply(this, arguments);
            this.on('list_view_loaded', this, function(data) {
                if(self.__parentedParent.$el.find('.oe_generate_po').length == 0
                    //将此处的purchase.order,更换为任何你想要添加按钮的表名
                    && self.dataset.model == 'purchase.order'){
                    var button = $("<button type='button' class='oe_button oe_highlight oe_generate_po'>导出模板</button>")
                        .click(this.proxy('create_logistics_bill'));
                    self.__parentedParent.$el.find('.oe_breadcrumb_item').append(button);
                }
            });
        },
        create_logistics_bill: function () {
            var self=this;
            var ctx = this.ViewManager.action.context;
            var active_records = this.groups.get_selection();
            ctx['active_records'] = active_records;
//                   此处为调用增加按钮模块的api 可酌情使用
//             new instance.web.Model(self.dataset.model).call("action_get_product_import_csv", [false, ctx]).
//                             then(function(result) {
//                         var res_id = result;
//                                 window.location.href = res_id['url']
//                    });
//                   此处为调用此模块的api   可酌情使用
              new instance.web.Model('tree_add_button.tree_add_button').call("action_get_product_import_csv", [false, ctx]).
                            then(function(result) {
                        var res_id = result;
                                window.location.href = res_id['url']
                   });
        },

    });

};
