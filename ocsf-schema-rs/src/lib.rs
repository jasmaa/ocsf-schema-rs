use typify::import_types;

use serde::{Deserialize, Serialize};

import_types!(schema = "all.json", struct_builder = true);
