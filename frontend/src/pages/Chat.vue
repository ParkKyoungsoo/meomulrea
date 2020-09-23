<template>
<div id="app">
	<v-app id="inspire">
		<v-container class="grey lighten-5">
			<v-row no-gutters>
				<v-col cols="3">
					<v-card max-width="500" class="mx-auto">
						<v-toolbar color="deep-purple accent-4" dark>
							<v-app-bar-nav-icon></v-app-bar-nav-icon>
							<v-toolbar-title>New Chat</v-toolbar-title>
							<v-spacer></v-spacer>
							<v-btn icon>
								<v-icon>mdi-magnify</v-icon>
							</v-btn>
						</v-toolbar>
						<v-list subheader>
							<v-subheader>Recent chat</v-subheader>
							<v-list-item v-for="item in items" :key="item.title" @click="test()">
								<v-list-item-avatar>
									<v-img :src="item.avatar"></v-img>
								</v-list-item-avatar>
								<v-list-item-content>
									<v-list-item-title v-text="item.title"></v-list-item-title>
								</v-list-item-content>
								<v-list-item-icon>
									<v-icon :color="item.active ? 'deep-purple accent-4' : 'grey'">chat_bubble</v-icon>
								</v-list-item-icon>
							</v-list-item>
						</v-list>
						<v-divider></v-divider>
						<v-list subheader>
							<v-subheader>Previous chats</v-subheader>
							<v-list-item v-for="item in items2" :key="item.title" @click="test()">
								<v-list-item-avatar>
									<v-img :src="item.avatar"></v-img>
								</v-list-item-avatar>
								<v-list-item-content>
									<v-list-item-title v-text="item.title"></v-list-item-title>
								</v-list-item-content>
							</v-list-item>
						</v-list>
					</v-card>
				</v-col> 

				<v-col cols="6">
					<v-card class="mx-auto">
						<v-list rounded>
							<v-subheader>REPORTS</v-subheader>
							<v-list-item-group color="primary">
								<v-list-item v-for="(item, i) in messages" :key="i" :class="(item.sent ? 'text-right' : '')" >
										<v-chip pill v-if="item.sent">
										{{ item.msg }}
										<v-avatar right>
											<v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
										</v-avatar>
										</v-chip>
										<v-chip pill v-else>
										<v-avatar left>
											<v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
										</v-avatar>
										{{ item.msg }}
										</v-chip>
								</v-list-item>
								<v-list-item>
									<v-textarea append-outer-icon="send"
												@click:append-outer="sendMessage"
												v-model=messageNew.text
												class="mx-2" 
												label="Message to send" 
												rows="2"></v-textarea>
								</v-list-item>
							</v-list-item-group>
						</v-list>
					</v-card>
				</v-col>
				<v-col col="3">
					<v-card
    class="mx-auto"
    width="256"
    tile
  >
    <v-navigation-drawer permanent>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">John Leider</v-list-item-title>
            <v-list-item-subtitle>john@vuetifyjs.com</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-icon>mdi-menu-down</v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list
        nav
        dense
      >
        <v-list-item-group v-model="user_item" color="primary">
          <v-list-item
            v-for="(item, i) in user_items"
            :key="i"
          >
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title v-text="item.text"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-card>
				</v-col>
			</v-row>
		</v-container>
	</v-app>
</div>
</template>

<script>
export default {
  name: "Chat",
  data: () => ({
    items: [
      { active: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
      { active: true, title: 'Ranee Carlson', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
      { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
      { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' },
    ],
    items2: [
      { title: 'Travis Howard', avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg' },
    ],
    messageNew: {
        text: null
    },
    messages: [
        { msg: 'Real-Time', avatar: 'https://cdn.vuetifyjs.com/images/john.png', sent: false },
        { msg: 'Audience', avatar: 'https://cdn.vuetifyjs.com/images/john.png', sent: true },
        { msg: 'Conversions', avatar: 'https://cdn.vuetifyjs.com/images/john.png', sent: false },
        { msg: 'reaas', avatar: 'https://cdn.vuetifyjs.com/images/john.png', sent: false },
    ],
    
    user_item: 0,
    user_items: [
        { text: 'My Files', icon: 'mdi-folder' },
        { text: 'Shared with me', icon: 'mdi-account-multiple' },
        { text: 'Starred', icon: 'mdi-star' },
        { text: 'Recent', icon: 'mdi-history' },
        { text: 'Offline', icon: 'mdi-check-circle' },
        { text: 'Uploads', icon: 'mdi-upload' },
        { text: 'Backups', icon: 'mdi-cloud-upload' },
    ],
  }),
	methods:{
		sendMessage(){
			this.messages.push({
				msg: this.messageNew.text,
				avatar: 'https://cdn.vuetifyjs.com/images/john.png', 
				sent: true
			})
			this.messageNew.text = null;
        },
        test(){
            return;
        }
	}
}
</script>