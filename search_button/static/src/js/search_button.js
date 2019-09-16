openerp.search_button = function(instance) {
var QWeb = instance.web.qweb,
        _t = instance.web._t,
        _lt = instance.web._lt;
instance.web.ListView.include({
        init: function() {
            var self = this;
            this._super.apply(this, arguments);
            this.on('list_view_loaded', this, function(data) {
                if(self.__parentedParent.$el.find('.oe_generate_search').length == 0){
                    var button = $("<button type='button' class='oe_button oe_highlight oe_generate_search'>高级搜索</button>")
                        .click(this.proxy('create_oe_searchview'));
                    self.__parentedParent.$el.find('.oe_searchview_unfold_drawer').append(button);
                }

            });
        },
       
            create_oe_searchview: function () {
                if (this.drawer)
                this.drawer.toggle();
            }


    });
instance.web_kanban.KanbanView.include({
            init: function() {
                var self = this;
                this._super.apply(this, arguments);
                this.on('kanban_view_loaded', this, function(data) {
                    if(self.__parentedParent.$el.find('.oe_generate_search').length == 0){
                        var button = $("<button type='button' class='oe_button oe_highlight oe_generate_search'>高级搜索</button>")
                            .click(this.proxy('create_oe_searchview_t'));
                        self.__parentedParent.$el.find('.oe_searchview_unfold_drawer').append(button);
                    }
    
                });
            },
           
                create_oe_searchview_t: function () {
                    if (this.drawer)
                    this.drawer.toggle();
                }
    
    
        });
};
